// <copyright file="Program.cs" company="Stefan Schukat">
// Copyright (c) Stefan Schukat. All rights reserved.
// Licensed under the MIT license. See LICENSE file in the project root for full license information.
// </copyright>

namespace EmbeddingPython
{
    using System;
    using System.IO;
    using System.Runtime.InteropServices;
    using Microsoft.Win32;
    using Python.Runtime;

    /// <summary>
    /// Class which contains the entry point for the program.
    /// </summary>
    internal static class Program
    {
        [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
        [return: MarshalAs(UnmanagedType.Bool)]
        private static extern bool SetDllDirectory(string pathName);

        /// <summary>
        /// Returns the installation path of an installed Python 3.6 64 Bit from the registry.
        /// </summary>
        /// <returns>Path to Python installtion or null if not found.</returns>
        private static DirectoryInfo GetPythonInstallationPathFromRegistry()
        {
            DirectoryInfo installationPath = null;

            using (var localMachineKey = RegistryKey.OpenBaseKey(RegistryHive.LocalMachine, RegistryView.Registry64))
            {
                using (var installPathKey = localMachineKey.OpenSubKey(@"SOFTWARE\Python\PythonCore\3.6\InstallPath"))
                {
                    var installationPathValue = installPathKey?.GetValue(null) as string;
                    installationPath = new DirectoryInfo(installationPathValue);
                }
            }

            return installationPath;
        }

        /// <summary>
        /// Sets up the path to an existing Python Enviroment.
        /// </summary>
        /// <returns>True if an existing python installation was found.</returns>
        private static bool PreparePythonEnvironment()
        {
            var installationPath = GetPythonInstallationPathFromRegistry();
            if (installationPath != null && installationPath.Exists)
            {
                return SetDllDirectory(installationPath.FullName);
            }

            return false;
        }

        /// <summary>
        /// Returns the type nam eof a Python object as a string.
        /// </summary>
        /// <param name="handle">Handle to the Pyhton object.</param>
        /// <returns>Name of the Python object.</returns>
        private static string GetPythonTypeName(IntPtr handle)
        {
            using (var excType = new PyObject(handle))
            {
                using (var typeName = excType.GetAttr("__name__"))
                {
                    return typeName.ToString();
                }
            }
        }

        /// <summary>
        /// Runs a simple python interactive loop in a console.
        /// </summary>
        private static void RunSimpleInteractiveLoop()
        {
            if (PreparePythonEnvironment())
            {
                PythonEngine.Initialize();

                if (PythonEngine.IsInitialized)
                {
                    var localEnvironment = new PyDict();

                    Console.WriteLine($"Python {PythonEngine.Version} in a .NET shell\nType exit() to exit.");

                    while (true)
                    {
                        Console.Write(">>> ");
                        var command = Console.ReadLine();
                        if (command == "exit()")
                        {
                            break;
                        }

                        try
                        {
                            try
                            {
                                // First try evaluation
                                var result = PythonEngine.Eval(command, locals: localEnvironment.Handle);
                                Console.WriteLine(result.ToString());
                            }
                            catch (PythonException exc) when (GetPythonTypeName(exc.PyType) == "SyntaxError")
                            {
                                // Try exec statement
                                PythonEngine.Exec(command, locals: localEnvironment.Handle);
                            }
                        }
                        catch (PythonException exc)
                        {
                            Console.WriteLine(exc.Message);
                        }
                    }

                    PythonEngine.Shutdown();
                }
            }
        }

        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        /// <param name="args">Command line arguments for the application.</param>
        private static void Main(string[] args)
        {
            RunSimpleInteractiveLoop();
        }
    }
}
