#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    i = j = 0
    while i < len(matrix):
        while j < len(matrix[i]):
            if j != len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][j]), end=" ")
            else:
                print("{:d}".format(matrix[i][j]), end="")
            j += 1
        print("")
        j = 0
        i += 1
