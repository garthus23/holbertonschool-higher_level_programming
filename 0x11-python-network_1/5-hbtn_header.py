#!/usr/bin/python3


""" module urllib """
import requests
import sys


"""
        script that fetches an url
"""


if __name__ == "__main__":
    if len(sys.argv) == 2:
        response = dict(requests.get(sys.argv[1]).headers)
        print(response.get('X-Request-Id'))
