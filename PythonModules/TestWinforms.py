#  
# Copyright (c) Stefan Schukat. All rights reserved.  
# Licensed under the MIT License. See LICENSE file in the project root for full license information.  
#  

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("UILibrary") 

import System.Windows.Forms as WinForms
import UILibrary
from System import Action


class WinFormsTest:
    def __init__(self):
        self.MainForm = UILibrary.MainForm()
        self.MainForm.PythonCallBack = Action(self.CallBack)
        app = WinForms.Application
        app.Run(self.MainForm)

    def CallBack(self):
        """Button click event handler"""
        print("Button clicked!")

if __name__ == '__main__':
    ui = WinFormsTest()