#!/usr/bin/python3



""" module urllib """
import requests



""""
	script that fetches an url
"""


if __name__ == "__main__":

    response = requests.get('https://intranet.hbtn.io/status').text
    print('Body response:')
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
