#!/usr/bin/python3


""" module sys and urllib """
import urllib.request
import sys


"""
    Request url and display X-Request-Id
"""

if __name__ == "__main__":

    if len(sys.argv) == 2:
        with urllib.request.urlopen(sys.argv[1])  as response:
            header=dict(response.info())
            print(header['X-Request-Id'])
