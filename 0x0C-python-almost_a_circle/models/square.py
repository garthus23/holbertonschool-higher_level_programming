#!/usr/bin/python3
""" module rectangle """
from models.rectangle import Rectangle


"""
    Square Class
"""


class Square(Rectangle):
    """ Classs Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ init function """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ getter size """
        return self.__size

    @size.setter
    def size(self, size):
        """ setter size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def __str__(self):
        """ str function """
        str1 = "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)
        return str1

    def update(self, *args, **kwargs):
        """ update method """
        if len(args) >= 1:
            for i in range(len(args)):
                if len(args) >= 1:
                    self.id = args[0]
                if len(args) >= 2:
                    self.size = args[1]
                if len(args) >= 3:
                    self.x = args[2]
                if len(args) == 4:
                    self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """" to_dictionary method """
        dicto = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return dicto
