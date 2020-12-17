#!/usr/bin/python3


def roman_to_int(roman_string):

    if roman_string is None:
        return (None)
    n = 0
    for i in roman_string:
        if i == 'V':
            n = n + 5
        if i == 'I':
            n = n + 1
        if i == 'X':
            n = n + 10
        if i == 'L':
            n = n + 50
        if i == 'C':
            n = n + 100
        if i == 'D':
            n = n + 500
        if i == 'M':
            n = n + 1000
    return (n)
