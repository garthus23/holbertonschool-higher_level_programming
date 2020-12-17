#!/usr/bin/python3


def roman_to_int(roman_string):

    if roman_string is None:
        return (None)
    n = 0
    for i in roman_string:
        if i == 'V':
            n = n + 5
        elif i == 'I':
            n = n + 1
        elif i == 'X':
            n = n + 10
        elif i == 'L':
            n = n + 50
        elif i == 'C':
            n = n + 100
        elif i == 'D':
            n = n + 500
        elif i == 'M':
            n = n + 1000
        else:
            return (None)
    return (n)
