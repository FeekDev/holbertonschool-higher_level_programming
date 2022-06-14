#!/usr/bin/python3
""" model with class rectangle"""
from models.base import Base


class Rectangle(Base):
    """class rectangle inherits Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    """getters and setters"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_attributes("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_attributes("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_attributes("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_attributes("y", value)
        self.__y = value
    """ validate """
    def validate_attributes(self, name, value, eq=True):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if eq and value < 0:
            raise ValueError(f"{name} must be >= 0")
        elif not eq and value <= 0:
            raise ValueError(f"{name} must be > 0")
    """ return the area"""
    def area(self):
        return self.__width * self.__height
    """ Display the area"""
    def display(self):
        for i in range(self.__height):
            print(self.__width * '#')
    def __str__()
