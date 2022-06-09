#!/usr/bin/python3
"""
Checks if is instance or subclass
"""


def is_kind_of_class(obj, a_class):
    """
    Return True : if the object is an instance
    of or if the object is subclass
    ----
    otherwhise return false
    """
    if type(obj) == a_class:
        return True
    if issubclass(type(obj), a_class):
        return True
