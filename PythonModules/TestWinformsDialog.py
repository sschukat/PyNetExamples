#  
# Copyright (c) Stefan Schukat. All rights reserved.  
# Licensed under the MIT License. See LICENSE file in the project root for full license information.  
#  

import clr
clr.AddReference("UILibrary") 
import UILibrary
from System import Action

def CallBack():
    """Button click event handler"""
    print("Button clicked!")

MainForm = UILibrary.MainForm()
MainForm.PythonCallBack = Action(CallBack)
MainForm.ShowDialog()