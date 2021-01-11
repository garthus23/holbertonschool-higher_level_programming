#!/usr/bin/python3


"""
    class Rectangle
"""


class Rectangle:
    """ class of rectangle """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ init rectangle """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        return (self.__width * self.__height)

    def perimeter(self):
        """ perimeter calc """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ str method """
        if self.__width or self.__height != 0:
            if isinstance(self.print_symbol, str):
                    str1 = ""
            if isinstance(self.print_symbol, list):
                    str1 = []
            for i in range(self.__height):
                if isinstance(self.print_symbol, str):
                    str1 = (str1 + self.print_symbol * self.__width)
                    if i is not self.__height - 1:
                        str1 = str1 + '\n'
                if isinstance(self.print_symbol, list):
                    str1 = (str(self.print_symbol) * self.__width *
                            self.__height)
        return str1

    def bigger_or_equal(rect_1, rect_2):
        if not type(rect_1) == Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not type(rect_2) == Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    def __repr__(self):
        """ repr method """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ destructor method (are you Sarah Connor ?) """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
