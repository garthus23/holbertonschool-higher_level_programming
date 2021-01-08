#!/usr/bin/python3


"""
    say_my_name function that say the name
    Attributes: first_name(str), last_name(str)
    Return: Nothing
"""


def say_my_name(first_name, last_name=""):
    """
    say the name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
