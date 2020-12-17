#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        maxkey = max(a_dictionary, key=a_dictionary.get)
        return (maxkey)
    else:
        return (None)
