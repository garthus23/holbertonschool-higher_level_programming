#!/usr/bin/python3


"""
    add to json
"""


if __name__ == "__main__":
    """ main function """
    from sys import argv
    import json
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    read_file = __import__('0-read_file').read_file

    list1 = []

    try : 
        with open('add_item.json', 'r') as f:
            for line in f:
                 list1 = json.loads(line)
    except:
        pass

    for i in range(len(argv)):
        if i > 0:
            list1.append(argv[i])

    save_to_json_file(list1, 'add_item.json')
