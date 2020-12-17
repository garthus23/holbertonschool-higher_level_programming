#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    newlist = []

    for i in range(5):

    # Append an empty sublist inside the list
        newlist.append([])

    for j in range(5):
        newlist[i].append(j)

    print(newlist)
