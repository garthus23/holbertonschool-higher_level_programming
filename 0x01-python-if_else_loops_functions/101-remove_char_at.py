#!/usr/bin/python3


def remove_char_at(str, n):
    newstr = ""
    a = 0
    for i in str:
        if a != n:
            newstr = newstr + chr(ord(i))
        a+= 1
    return(newstr)
