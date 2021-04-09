#!/usr/bin/python3


""" module urllib """
import requests
import sys


"""
        script that fetches an url
"""


if __name__ == "__main__":
    if len(sys.argv) == 3:
        response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
        print(response.text)
