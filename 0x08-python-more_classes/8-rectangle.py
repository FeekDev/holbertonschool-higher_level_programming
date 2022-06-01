#!/usr/bin/python3
"""
This module define a Rectangle based in the
previous module
"""


class Rectangle:
    """
    This class contain constructor and methods
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        The method constructor:
        Parameters:
        width: the purpose is set the value
        height: the purpose is set the value
        """
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    def __str__(self):
        """Print string good to view"""
        if self.__width == 0 or self.__height == 0:
            return ""
        w = self.width
        h = self.height
        return ((str(self.print_symbol) * w + '\n') * h)[:-1]

    def __repr__(self):
        """new instance based on representation"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """Destructor"""
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

    @property
    def width(self):
        """The getter parameters: itself"""
        return self.__width

    @width.setter
    def width(self, value):
        """The setter parameters: value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The getter parameters: itself"""
        return self.__height

    @height.setter
    def height(self, value):
        """The setter parameters: value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area width*height """
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter 2(width+height) """
        if not self.__width or not self.__height:
            return 0
        return (self.__width + self.__height) * 2

    @staticmethod
    def bigger_or_equal(rec_1, rec_2):
        '''Returns the bigger of two rectangles.
        Args:
            rec_1: first rectangle.
            rec_2: second rectangle.
        '''
        if type(rec_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rec_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rec_1.area() < rec_2.area():
            return rec_2
        return rec_1
