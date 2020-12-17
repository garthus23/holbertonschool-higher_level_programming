#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    c = []
    for ele in set_1:
        if ele not in set_2:
            c.append(ele)

    for ele in set_2:
        if ele not in set_1:
            c.append(ele)
    return (c)
