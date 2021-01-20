#!/usr/bin/python3


"""
    Read file function
"""


def read_file(filename=""):
    """ Read file function """
    with open(filename) as f:
        for line in f:
            print(line, end="")
        f.close()
