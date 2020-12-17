#!/usr/bin/python3


def copy_2d(p):
    return [list(p2) for p2 in p]


def square_matrix_simple(matrix=[]):

    array = copy_2d(matrix)
    i = 0
    j = 0
    while i < len(array):
        while j < len(array[i]):
            array[i][j] *= array[i][j]
#            print(array[i][j])
            j += 1
        j = 0
        i += 1
    return (array)
