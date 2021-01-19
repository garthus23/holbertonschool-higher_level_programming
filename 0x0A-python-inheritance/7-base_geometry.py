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
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
