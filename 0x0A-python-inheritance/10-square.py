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
        if not isinstance(value, int) or value is True:
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

    def area(self):
        """ area method to calcul area """
        return(self.__height * self.__width)

    def __str__(self):
        """ str to print the str """
        return("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """ give the square """
    def __init__(self, size):
        """init square """
        BaseGeometry.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        """ area method to calcul area """
        return (self.__size * self.__size)

    def __str__(self):
        """ str to print the str """
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
