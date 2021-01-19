#!/usr/bin/python3


"""
    BaseGeometry empty class
"""


class BaseGeometry():
    """ base geometry class """
    def area(self):
        """ area definition """
        raise TypeError("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validator """
        if not isinstance(value, int) or value == True:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ Rectangle Class """
    def __init__(self, width, height):
        """ init function """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height



