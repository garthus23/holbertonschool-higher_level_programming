#!/usr/bin/python3

"""
	find the peak
"""

def find_peak(list_of_integers):
    """ find the max on a list """
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
