#  
# Copyright (c) Stefan Schukat. All rights reserved.  
# Licensed under the MIT License. See LICENSE file in the project root for full license information.  
#  

import clr
import System
import System.Windows.Forms
import System.Drawing

class MainForm(System.Windows.Forms.Form):
    def __init__(self):
        self.InitializeComponent()

    def ButtonCallPython_Click(self, source, args):
        print("Button clicked")

    def InitializeComponent(self):
        self.buttonCallPython = System.Windows.Forms.Button()
        self.SuspendLayout()

        self.buttonCallPython.Location = System.Drawing.Point(12, 12)
        self.buttonCallPython.Name = "buttonCallPython"
        self.buttonCallPython.Size = System.Drawing.Size(75, 23)
        self.buttonCallPython.TabIndex = 0
        self.buttonCallPython.Text = "Call Python"
        self.buttonCallPython.UseVisualStyleBackColor = True
        self.buttonCallPython.Click += System.EventHandler(self.ButtonCallPython_Click)

        self.AutoScaleDimensions = System.Drawing.SizeF(6.0, 13.0)
        self.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        self.ClientSize = System.Drawing.Size(245, 44)
        self.Controls.Add(self.buttonCallPython)
        self.MaximizeBox = False
        self.MinimizeBox = False
        self.Name = "MainForm"
        self.Text = "TestWinforms"
        self.ResumeLayout(False)


if __name__ == "__main__":
    m = MainForm()
    m.ShowDialog()