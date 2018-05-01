﻿// <copyright file="Program.cs" company="Stefan Schukat">
// Copyright (c) Stefan Schukat. All rights reserved.
// Licensed under the MIT license. See LICENSE file in the project root for full license information.
// </copyright>

namespace SimpleDialog
{
    using System;
    using System.Windows.Forms;

    /// <summary>
    /// Class which contains the entry point for the program.
    /// </summary>
    internal static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        private static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new UILibrary.MainForm());
        }
    }
}
