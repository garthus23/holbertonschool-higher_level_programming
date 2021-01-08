#!/usr/bin/python3


import numpy as np
"""
    Matrix multiplication
    Attributes: m_a(matrix): first matrix m_b(matrix): second matrix
    Return result(matrix)
"""


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrix m_a * m_b
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if m_a == [[]] or m_a == []:
        raise ValueError("m_a can't be empty")

    if m_b == [[]] or m_b == []:
        raise ValueError("m_b can't be empty")
    for i in range(len(m_a)):
        if len(m_a[0]) is not len(m_a[i]):
            raise TypeError("each row of m_a must be of the same size")
        for j in range(len(m_a[i])):
            if not isinstance(m_a[i][j], (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for i in range(len(m_b)):
        if len(m_b[0]) is not len(m_b[i]):
            raise TypeError("each row of m_b must be of the same size")
        for j in range(len(m_b[i])):
            if not isinstance(m_b[i][j], (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    if len(m_a) < len(m_b):
        result = [[0 for x in range(len(m_a[0]))] for y in range(len(m_a))]
    else:
        result = [[0 for x in range(len(m_b[0]))] for y in range(len(m_b))]
    try:
        result = np.dot(m_a,m_b)
    except ValueError:
        print("m_a and m_b can't be multiplied")
    return result
