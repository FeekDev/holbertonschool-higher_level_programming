#!/usr/bin/python3
"""
check an instance of a class that inherited (dir. or indir.)
"""


def inherits_from(obj, a_class):
    """
     returns True if is - return false otherwise
    """
    return isinstance(obj, a_class) and type(obj) != a_class
