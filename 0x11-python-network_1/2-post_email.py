#!/usr/bin/python3


""" module sys and urllib """
import urllib.request
import urllib.parse
import sys


"""
    Request url and display X-Request-Id
"""

if __name__ == "__main__":

    if len(sys.argv) == 3:
        data = {
        'email': sys.argv[2]
        }
        data = bytes(urllib.parse.urlencode(data).encode())
        with urllib.request.urlopen(sys.argv[1], data)  as response:
            print(response.read().decode('utf-8'));
