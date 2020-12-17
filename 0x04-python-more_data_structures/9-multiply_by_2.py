#!/usr/bin/python3


def multiply_by_2(a_dictionary):

    newdict = a_dictionary.copy()
    for i in newdict:
        newdict[i] *= 2

    return (newdict)
