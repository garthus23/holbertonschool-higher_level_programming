#!/usr/bin/python3


"""
    class of square
"""


class Square:
    """
    Class that define a Square

    Attributes:
        size(size): this is the size
    """

    def __init__(self, size):
        self.set_size(size)

    def get_size(self):
        return self.__size

    def set_size(self, size=0):
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        for i in range(0, self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print('')

    size = property(get_size, set_size)
