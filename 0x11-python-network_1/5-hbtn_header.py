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
            with requests.get(sys.argv[1]) as response:
                if response:
                    print(dict(response.headers).get('X-Request-Id'))
        except:
            pass
