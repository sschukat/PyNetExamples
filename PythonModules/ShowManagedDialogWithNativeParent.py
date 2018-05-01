#  
# Copyright (c) Stefan Schukat. All rights reserved.  
# Licensed under the MIT License. See LICENSE file in the project root for full license information.  
#  

def ShowDialog(parentHandle):
    import clr
    import System
    import System.Windows

    openFileDialog = System.Windows.Forms.OpenFileDialog();
    openFileDialog.InitialDirectory = "c:\\"
    openFileDialog.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*"
    openFileDialog.FilterIndex = 2
    openFileDialog.RestoreDirectory = True

    w = None
    try:
        i = System.Int32(CurrentHandle)
        mainWindowHandle = System.IntPtr.op_Explicit(i)
        w = System.Windows.Forms.NativeWindow()
        w.AssignHandle(mainWindowHandle)
    except:
        import traceback
        traceback.print_exc()
    if w:
        openFileDialog.ShowDialog(w)
    else:
        openFileDialog.ShowDialog()

if __name__ == "__main__":
    import win32ui
    ShowDialog(win32ui.GetMainFrame().GetSafeHwnd())