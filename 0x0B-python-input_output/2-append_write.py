#!/usr/bin/python3


"""
    add string to a file
"""


def append_write(filename="", text=""):
    """ add string to a file """
    with open(filename, 'a') as f:
        ln = f.write(text)
        f.close()
        return (ln)
