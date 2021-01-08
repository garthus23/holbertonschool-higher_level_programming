#!/usr/bin/python3


def text_indentation(text):
    
    i = 0
    while i+1 != len(text):

        if text[i+1] == ' ' and text[i] == ' ':
                i += 1
        elif text[i-1] == '.' or text[i-1] == '?' or text[i-1] == ':' and text[i] == ' ':
                i += 1
        elif text[i] == '.' or text[i] == '?' or text[i] == ':':
            print("{:s}".format(text[i]), end="")
            print("\n")
            i += 1
        else:
            print("{:s}".format(text[i]), end="")
            i += 1
    if text[i] != ' ':
        print("{:s}".format(text[i]), end="")
