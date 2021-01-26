#!/usr/bin/python3


"""
    base of all other classes
"""
import json


class Base:
    """ base of all other classes """

    __nb_objects = 0

    def __init__(self, id=None):
        """ init function """
        self.id = id

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ list to json """
        if list_dictionaries is None:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ class methode to save to file """
        list1 = []
        for i in list_objs:
            list1.append(cls.to_json_string(cls.to_dictionary(i)))
        name = "{}.json".format(cls.__name__)
        with open(name, "w") as f:
            f.write(str(list1))

    def from_json_string(json_string):
        """ json to string """
        if json_string is None:
            return ('[]')
        else:
            return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ dictionary to instance """
        for key, value in dictionary.items():
            setattr(cls, key, value)

    @classmethod
    def update(cls, *args, **kwargs):
        if len(args) >= 1:
            for i in range(len(args)):
                if len(args) >= 1:
                    cls.id = args[0]
                if len(args) >= 2:
                    cls.__width = args[1]
                if len(args) >= 3:
                    cls.__height = args[2]
                if len(args) >= 4:
                    cls.__x = args[3]
                if len(args) == 5:
                    cls.__y = args[4]
        else:
            for key, value in kwargs.items():
                    setattr(cls, key, value)

    @classmethod
    def load_from_file(cls):
        name = "{}.json".format(cls.__name__)
        with open(name, 'r') as f:
            list1 = f.readlines()

        return (list(list1))
