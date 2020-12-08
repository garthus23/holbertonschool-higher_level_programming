#!/usr/bin/python3


def print_last_digit(number):

    if number > 0:
        print(number % 10, end="")
        return(number % 10)
    if number == 0:
        print(number, end="")
        return(number)
    if number < 0:
        print((-number) % 10, end="")
        return(-number % 10)
