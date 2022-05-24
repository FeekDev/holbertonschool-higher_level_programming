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
    private
    """
    def __init__(self, size):
        """
        Parameters:
        ----------
        size = is a private instance attribute
        to allow the square size.
        """
        self._Square__size = size


'print(__import__("0.square.py").__doc__)'
'print(__import__("0.square.py").Square.__doc__)'
'print(__import__("0.square.py").Square._init_.__doc__)'
