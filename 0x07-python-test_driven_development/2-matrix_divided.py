#!/usr/bin/python3


"""
    matrix_divided: divide all elements of a matrix
    Attributes: matrix(list): list of int, div(int): number used to divide
    Return: new matrix
"""


def matrix_divided(matrix, div):
    """
    function: divide list of integer
    """
    mustbeint = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = []
    new_matrix = list(map(list, matrix))

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zeo")
    for i in range(len(matrix)):
        if len(matrix[i]) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError(mustbeint)
            new_matrix[i][j] = round((new_matrix[i][j] / div), 2)
    return (new_matrix)
