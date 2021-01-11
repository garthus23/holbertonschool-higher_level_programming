#!/usr/bin/python3


"""
    Class that defines Rectangle
"""


class Rectangle:
    """
    Class Rectangle
    """
    def __init__(self, width=0, height=0):
        """ init section """
        self.height = height
        self.width = width

    @property
    def height(self):
        """ getter height """
        return self.__height

    @property
    def width(self):
        """ getter width """
        return self.__width

    @height.setter
    def height(self, height):
        """ setter height """
        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("width must be >= 0")
        self.__height = height

    @width.setter
    def width(self, width):
        """ setter width """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
