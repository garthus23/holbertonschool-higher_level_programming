#!/usr/bin/python3



""" module urllib """
import requests
import sys



""""
	script that fetches an url
"""


if __name__ == "__main__":

    response = dict(requests.get('https://intranet.hbtn.io/status').headers)
    print(response['X-Request-Id'])
