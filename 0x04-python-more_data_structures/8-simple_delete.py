#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):

    for i in a_dictionary:
        if i == key:
            a_dictionary.pop(key, None)
            break
    return (a_dictionary)
