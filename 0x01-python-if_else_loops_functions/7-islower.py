#!/usr/bin/python3


def islower(c):
    if c:
        for i in range(ord('a'), ord('z')+1):
            if chr(i) == c:
                return(True)
    return(False)
