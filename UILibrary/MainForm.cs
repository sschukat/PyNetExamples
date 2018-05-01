// <copyright file="MainForm.cs" company="Stefan Schukat">
// Copyright (c) Stefan Schukat. All rights reserved.
// Licensed under the MIT license. See LICENSE file in the project root for full license information.
// </copyright>

namespace UILibrary
{
    using System;
    using System.Windows.Forms;

    /// <summary>
    /// Sample form which is created by Python.NET a uses a callback for communication.
    /// </summary>
    public partial class MainForm : Form
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="MainForm"/> class>
        /// </summary>
        public MainForm()
        {
            this.InitializeComponent();
        }

        /// <summary>
        /// Gets or sets the delegate to be access by Python.
        /// </summary>
        public Action PythonCallBack { get; set; }

        /// <summary>
        /// Event handler which calls into Python code.
        /// </summary>
        /// <param name="sender">Button which is clicked.</param>
        /// <param name="e">Eventarguments for the call (not used)</param>
        private void ButtonCallPython_Click(object sender, System.EventArgs e) => this.PythonCallBack?.Invoke();
    }
}
