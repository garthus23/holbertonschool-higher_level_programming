#!/usr/bin/python3


""" module urllib """
import requests
import sys


"""
    script that fetches an url
"""


if __name__ == "__main__":
    if len(sys.argv) == 2:
        response = requests.get(sys.argv[1])
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))
        else:
            print("{}".format(response.text))
