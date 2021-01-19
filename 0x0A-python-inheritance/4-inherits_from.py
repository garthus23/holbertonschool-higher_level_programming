#!/usr/bin/python3


"""
    object is an instance of a class ?
"""


def inherits_from(obj, a_class):
    """  object is an instance of a class ? """

    return (issubclass(type(obj), a_class))
