#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    mylist = []
    if len(tuple_a) == 2 and len(tuple_b) == 2:
        list_add = tuple_a + tuple_b
    for i in range(0, 2):
            if i < len(tuple_a):
                mylist.append(tuple_a[i])
            else:
                mylist.append(0)
    for i in range(0, 2):
            if i < len(tuple_b):
                mylist.append(tuple_b[i])
            else:
                mylist.append(0)

    return (mylist[0] + mylist[2], mylist[1] + mylist[3])
