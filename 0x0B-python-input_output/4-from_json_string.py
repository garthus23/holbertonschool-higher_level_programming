#!/usr/bin/python3


"""
    JSON string to Object
"""


def from_json_string(my_obj):
    """ to_json_string """
    import json
    return(json.loads(my_obj))
