# PyNetExamples
Examples for migration and interop issues with Python.NET. There are functional example and examples which show how to integrate WinForms UI into Python.

## Functional 
* Checkenum.py : A class which translates form .NET enums to Python enums to have textual representation and value handling. 
* MarshalComObject.py : A class which marshals a win32com dispatch Python object to a .NET __COMObject.
* netdict.py : A Python dictionary extension class which provides a method to convert the Python dictionary to a .NET generic dictionary.

## UI Examples
* ShowManagedDialogWithNativeParent.py: Show how to create a .NET dialog with the parent window handle from a PythonWin based application.
* TestWinforms.py: Creates a simple application startup routine which uses the dialog defined in the contained UILibrary solution, which provides a simple WinForms dialog to interact with Python.
* TestWindormsDialog.py : Simple script just to show the dialog defined in the contained UILibrary solution, which provides a simple WinForms dialog to interact with Python.
* WinFormsPython.py : The dialog a in UILibrary fully defined in Python which uses the WinForms directly instead of using a designer.

## Embedding
The embedding Python solution shows to to create a simple REPL loop inside a .NET console application using the Python.Runtime assembly. 
