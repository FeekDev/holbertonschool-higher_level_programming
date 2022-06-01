#!/usr/bin/python3
"""
This module define a Rectangle based in the
previous module
"""


class Rectangle:
    """
    This class contain constructor and methods
    """
    def __init__(self, width=0, height=0):
        """
        The method constructor:
        Parameters:
        width: the purpose is set the value
        height: the purpose is set the value
        """
        self.height = height
        self.width = width

    def width(self):
        """The getter parameters: itself"""
        return self.__width

    def width(self, value):
        """The setter parameters: value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    width = property(width, width)

    def height(self):
        return self.__height
        """The getter parameters: itself"""

    def height(self, value):
        """The setter parameters: value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
    height = property(height, height)
