#  
# Copyright (c) Stefan Schukat. All rights reserved.  
# Licensed under the MIT License. See LICENSE file in the project root for full license information.  
#  

def MarshalPyComToClr(sourceObject):
    """Converts the given win32com Dispatch object to a corresponding .NET object"""
    import pythoncom
    import re
    import clr
    import System
    import System.Runtime.InteropServices as InteropServices

    IDispatch = None
    if hasattr(sourceObject, "_oleobj_"):
        IDispatch = sourceObject._oleobj_
    elif (hasattr(sourceObject, "__name__" and sourceObject.__name__ == 'PyIDispatch')):
        IDispatch = sourceObject
    else:
        raise TypeError("win32com.client.Dispatch or pythoncom.PyIDispatch object exspected.")
    match = re.match("<PyIDispatch at (?P<obj>[0-9XA-F]+) with obj at (?P<address>[0-9XA-F]+)>", repr(IDispatch), re.IGNORECASE)
    if not match:
        raise TypeError("Retreiving address of PyCom object failed.")
    address = int(match.group("address"), 16)
    netAddress = None
    if System.Environment.Is64BitProcess:
        netAddress = System.IntPtr.Overloads[System.Int64](address)
    else:
        netAddress = System.IntPtr.Overloads[System.Int32](address)
    comObject = InteropServices.Marshal.GetObjectForIUnknown(netAddress)
    return comObject

if __name__ == "__main__":
    from win32com.client import Dispatch
    App = Dispatch("Word.Application")
    NetApp = MarshalPyComToClr(App)
    print(NetApp)