#!/usr/bin/python3


"""
    write a file
"""


def write_file(filename="", text=""):
    """ write a file """
    with open(filename, 'w') as f:
        ln = f.write(text)
        f.close()
        return (ln)
