#!/usr/bin/python3


def search_replace(my_list, search, replace):

    newlist = []
    i = 0
    while i is not (len(my_list)):
        if my_list[i] == search:
            newlist.append(replace)
        else:
            newlist.append(my_list[i])
        i += 1
    return (newlist)
