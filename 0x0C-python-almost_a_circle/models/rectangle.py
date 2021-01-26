#!/usr/bin/python3


"""
    Rectangle Class
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init rectangle """
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter width """
        return self.__width

    @property
    def height(self):
        """ getter height """
        return self.__height

    @property
    def x(self):
        """ getter x """
        return self.__x

    @property
    def y(self):
        """ getter y """
        return self.__y

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
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """ setter x """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """ setter y """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ area calc """
        return (self.__width * self.__height)

    def display(self):
        """ display Rect """
        if self.__width or self.__height != 0:
            for i in range(self.__y):
                print('')
            for i in range(self.__height):
                print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ str method """
        str1 = "[Rectangle] (" + str(self.id) + ") " + str(self.__x) + "/" + \
            str(self.__y) + " - " + str(self.__width) + "/" + \
            str(self.__height)
        return str1

    def update(self, *args, **kwargs):
        if len(args) >= 1:
            for i in range(len(args)):
                if len(args) >= 1:
                    self.id = args[0]
                if len(args) >= 2:
                    self.__width = args[1]
                if len(args) >= 3:
                    self.__height = args[2]
                if len(args) >= 4:
                    self.__x = args[3]
                if len(args) == 5:
                    self.__y = args[4]
        else:
            for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        return ({
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
                })
