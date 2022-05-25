#!/usr/bin/python3
"""
    This Module that defines a square
    ...
    th purpose is init the file for create
    a square
    """


class Square:
    """
    The class is for allow the size
    ...
    in this file the class have one attribute
    private, and check if is int or be > 0
    """
    def __init__(self, size=0):
        """
        Parameters:
        ----------
        size = is a private instance attribute
        to allow the square size.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size


'print(__import__("2.square.py").__doc__)'
'print(__import__("2.square.py").Square.__doc__)'
'print(__import__("2.square.py").Square._init_.__doc__)'
