#!/usr/bin/python3


"""
    add string to a file
"""


def append_write(filename="", text=""):
    with open(filename, 'a') as f:
        ln = f.write(text)
        f.close()
        return (ln)
