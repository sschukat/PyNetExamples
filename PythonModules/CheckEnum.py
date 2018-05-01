#  
# Copyright (c) Stefan Schukat. All rights reserved.  
# Licensed under the MIT License. See LICENSE file in the project root for full license information.  
#  

import clr
import re

__all__ = ("NetEnum", "ConstantTypes")

# ----------------------------------------------------------------------------
# Read only constants to define the type of enums used.
# ----------------------------------------------------------------------------
class _ConstantTypes(object):
    """Provides a read-only constant definition for the types of enums
    available."""
    def _get_enum(self):
        return 0

    def _get_flags(self):
        return 1

    # Create read only properties
    Enum = property(_get_enum, None, None, "Type is an enum")
    Flags = property(_get_flags, None, None, "Type is flags")

ConstantTypes = _ConstantTypes()

class _EnumItem(int):
    def __str__(self):
        """Returns the value as a string representation."""
        try:
            return self._names[self]
        except KeyError:
            return str(int(self))

    def __repr__(self):
        """Return the class instance as a string representation."""
        name = "Enumvalue"
        try:
            name = self._names[self]
        except KeyError:
            pass
        return '<%s %s>' % (name, int(self))


class _Enum(object):
    _type = ConstantTypes.Enum
    _itemclass = _EnumItem

    def __call__(self, value):
        try:
            return getattr(self, self._names[value])
        except KeyError:
            item = self._itemclass(value)
            item._names = self._names
            return item

    def __str__(self):
        return self.__repr__

    def __repr__(self):
        return "<%s enum>" % self.__class__.__name__


class _FlagsItem(int):
    def __str__(self):
        """Return the string equivalent for the flags."""
        v = int(self)
        values = []
        if v == 0:
            try:
                values.append(self._names[0])
            except (KeyError, IndexError):
                pass
        while v:
            bit = v & (~v+1)
            try:
                values.append(self._names[bit])
            except (KeyError, IndexError):
                values.append("<%s %s>" % ("Flagsvalue", v))
            v &= ~bit
        if not values:
            return '0'
        return '|'.join(values)

    def __repr__(self):
        """Return the class instance as a string representation."""
        return '<%d = %s>' % (int(self), str(self))

    def __or__(self, other):
        """Provides a bitwise or operation which results again in a flags"""
        val = type(self)(int(self) | int(other))
        val._names = self._names
        return val

    def __and__(self, other):
        """Provides a bitwise and operation which results again in a flags"""
        val = type(self)(int(self) & int(other))
        val._names = self._names
        return val

    def __xor__(self, other):
        """Provides a bitwise xor operation which results again in a flags"""
        val = type(self)(int(self) ^ int(other))
        val._names = self._names
        return val


class _Flags(object):
    _type = ConstantTypes.Flags
    _itemclass = _FlagsItem

    def __call__(self, value):
        item = self._itemclass(value)
        item._names = self._names
        return item

    def __str__(self):
        return self.__repr__

    def __repr__(self):
        return "<%s flags>" % self.__class__.__name__



class NetEnums(object):
    def __init__(self):
        pass

    @staticmethod
    def _determineEnumType(enum):
        if issubclass(enum, clr.System.Enum):
            basetype = clr.System.Type.GetType(re.split("'", repr(enum))[1])
            attributes = basetype.GetCustomAttributes(True)
            isFlag = any([isinstance(x, clr.System.FlagsAttribute) for x in attributes])
            return True, isFlag
        return false, false

    def Add(self, netEnum):
        """Creates a new enum attribute class and adds it to the internal
        cache"""
        isEnum, isFlag = NetEnums._determineEnumType(netEnum)
        if not isEnum:
            raise TypeError("Given element is not a net Enum.")
        BaseClass = _Enum
        if isFlag:
            BaseClass = _Flags

        enumname = re.split("\.", re.split("'", repr(netEnum))[1])[-1]
        enumvalues = dict(list(zip(clr.System.Enum.GetNames(netEnum), clr.System.Enum.GetValues(netEnum))))

        # Create class
        EnumClass = type(str(enumname), (BaseClass,), dict(_names=enumvalues,
                                                       __doc__="%s enumeration" % enumname))

        # Add attributes to the class
        for (name, value) in list(enumvalues.items()):
            _itemclass = EnumClass._itemclass
            itemvalue = _itemclass(value)
            itemvalue._names = enumvalues
            setattr(EnumClass, name, itemvalue)
            EnumClass._names[value] = name

        enumItem = EnumClass()
        internalName = "_" + enumname
        setattr(self, internalName, enumItem)

        def getter(self, Name=internalName):
            return getattr(self, Name)
        setattr(self.__class__, enumname, property(getter,
                                               None,
                                               None,
                                               enumItem.__doc__))

def NetEnum(netEnum):
    isEnum, isFlag = False, False
    if issubclass(netEnum, clr.System.Enum):
        basetype = clr.System.Type.GetType(re.split("'", repr(netEnum))[1])
        attributes = basetype.GetCustomAttributes(True)
        isFlag = any([isinstance(x, clr.System.FlagsAttribute) for x in attributes])
        isEnum, isFlag = True, isFlag
        
    if not isEnum:
        raise TypeError("Given element is not a net Enum.")

    BaseClass = _Enum
    if isFlag:
        BaseClass = _Flags

    enumname = re.split("\.", re.split("'", repr(netEnum))[1])[-1]
    enumvalues = dict(list(zip(clr.System.Enum.GetNames(netEnum), clr.System.Enum.GetValues(netEnum))))

    # Create class
    EnumClass = type(str(enumname), (BaseClass,), dict(_names=enumvalues,
                                                   __doc__="%s enumeration" % enumname))
    # Add attributes to the class
    for (name, value) in list(enumvalues.items()):
        _itemclass = EnumClass._itemclass
        itemvalue = _itemclass(value)
        itemvalue._names = enumvalues
        setattr(EnumClass, name, itemvalue)
        EnumClass._names[value] = name
    return EnumClass()        

if __name__ == "__main__":
    Constants = NetEnums()
    Constants.Add(clr.System.Base64FormattingOptions)
    Constants.Add(clr.System.AttributeTargets)
    print(int(Constants.AttributeTargets.Assembly | Constants.AttributeTargets.Constructor))
    AttributeTargets = NetEnum(clr.System.AttributeTargets)
    print(AttributeTargets.Assembly)
    print(AttributeTargets.Assembly | AttributeTargets.Constructor)
