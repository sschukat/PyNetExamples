#  
# Copyright (c) Stefan Schukat. All rights reserved.  
# Licensed under the MIT License. See LICENSE file in the project root for full license information.  
#  

import clr
from System.Collections.Generic import Dictionary
import System

class netdict(dict):
    def asManaged(self, neededKeyType = None, neededValueType = None):
        def CheckAllowedTypes(checkableList, listName):
            types = set([type(x) for x in checkableList])
            checktypes = set([x in (str, int, float) for x in types])
            if len(checktypes) != 1:
                raise TypeError("{0} in dictionary use wrong types".format(listName))
            if not checktypes:
                raise TypeError("{0} in dictionary use wrong types".format(listName))
            return tuple(types)

        typeMapping = {str : System.String, int : System.Int32, float : System.Double}

        keyTypes   = CheckAllowedTypes(self.keys(), "Keys")
        valueTypes = CheckAllowedTypes(self.values(), "Values")

        keyType = System.Object
        if len(keyTypes) == 1:
            keyType = typeMapping[keyTypes[0]]

        if neededKeyType and keyType != neededKeyType:
            raise TypeError("Provided key type does not match needed key type")

        valueType = System.Object
        if len(valueTypes) == 1:
            valueType = typeMapping[valueTypes[0]]

        if neededValueType and valueType != neededKeyType:
            raise TypeError("Provided value type does not match needed value type")

        managedDict = Dictionary[keyType, valueType]()
        for key, value in self.items():
            managedDict[key] = value
        return managedDict


def _DebugInfo(managedDict):
    print(managedDict)
    for x in managedDict.GetType().GetGenericArguments():
        print(x)
    for x in managedDict.Keys:
        print(x)
    for x in managedDict.Values:
        print(x)

if __name__ == "__main__":
    a = netdict({1 : 1, 2 : 2})
    managedDict = a.asManaged()
    _DebugInfo(managedDict)
    
    a = netdict(a = 1, b = 2)
    managedDict = a.asManaged()
    _DebugInfo(managedDict)

    a = netdict(a = 1, b = "a")
    managedDict = a.asManaged()
    _DebugInfo(managedDict)

    a = netdict(a = "a", b = "a")
    managedDict = a.asManaged()
    _DebugInfo(managedDict)

    a = netdict({1 : "b", "a" : 2})
    managedDict = a.asManaged()
    _DebugInfo(managedDict)

    a = netdict(a = 1, b = 2)
    try:
        managedDict = a.asManaged(System.String, System.Double)
    except TypeError as ex:
        print(ex)

    a = netdict(a = 1, b = 2)
    try:
        managedDict = a.asManaged(System.Int32, System.Int32)
    except TypeError as ex:
        print(ex)

