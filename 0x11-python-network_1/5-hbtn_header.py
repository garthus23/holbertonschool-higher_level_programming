#!/usr/bin/python3


""" module urllib """
import requests
import sys


"""
        script that fetches an url
"""


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            print(requests.get(sys.argv[1]).headers.get('x-request-id'))
        except:
            pass
