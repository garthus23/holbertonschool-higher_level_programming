#!/usr/bin/python3


"""
    student
"""


class Student:
    """ student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        my_dict = {}
        if isinstance(attrs, list):
            for i in attrs:
                try:
                    my_dict.update({i: self.__dict__[i]})
                except:
                    pass
        else:
            return (self.__dict__)
        return(my_dict)
