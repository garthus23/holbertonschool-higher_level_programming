#!/usr/bin/python3


"""
    class Rectangle
"""


class Rectangle:
    """ class of rectangle """

    def __init__(self, width=0, height=0):
        """ init rectangle """
        self.height = height
        self.width = width

    @property
    def width(self, width):
        """ getter width """
        return self.__width

    @property
    def height(self, height):
        """ getter height """
        return self.__height

    @width.setter
    def width(self, width):
        """ setter width """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """ setter height """
        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("width must be >= 0")
        self.__height = height

    def area(self):
        """ area calc """
        self.area = self.__width * self.__height
        return (self.area)

    def perimeter(self):
        """ perimeter calc """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2 + self.__height * 2)