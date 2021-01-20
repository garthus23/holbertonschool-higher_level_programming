#!/usr/bin/python3


"""
    writes an Object to a text file
"""


def save_to_json_file(my_obj, filename):
    """ save_to_json_file """
    import json
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
        f.close()
