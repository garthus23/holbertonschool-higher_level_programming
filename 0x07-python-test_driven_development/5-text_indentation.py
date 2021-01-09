#!/usr/bin/python3


"""
    text_indentation: auto indent text
    Attributes: test(str): string to process
    Return: None
"""


def text_indentation(text):
    """
    text_indentation that auto indent text
    """
    i = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    while i+1 != len(text):

        if text[i+1] == ' ' and text[i] == ' ':
                i += 1
        elif ((text[i-1] == '.' or text[i-1] == '?' or text[i-1] == ':') and
              text[i] == ' '):
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
