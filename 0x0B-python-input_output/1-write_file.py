#!/usr/bin/python3


"""
    write a file
"""


def write_file(filename="", text=""):
    with open(filename, 'w') as f:
        ln = f.write(text)
        f.close()
        return (ln)
