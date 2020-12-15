#!/usr/bin/python3


def no_c(my_string):

    result_str = ""
    for i in range(0, len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            result_str = result_str + my_string[i]
    return (result_str)
