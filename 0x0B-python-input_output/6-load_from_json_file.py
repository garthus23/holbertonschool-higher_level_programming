#!/usr/bin/python3


"""
    load_from_json_file
"""


def load_from_json_file(filename):
    """ load_from_json_file """
    import json
    with open(filename, 'r') as f:
        for line in f:
            return(json.loads(line))
