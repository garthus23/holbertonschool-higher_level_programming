#!/usr/bin/python3


""" module urllib """
import requests
import sys


""""
        script that fetches an url
"""


if __name__ == "__main__":
    if len(sys.argv) == 2:
        response = requests.post('http://0.0.0.0:5000/search_user', data={'q': sys.argv[1]}).json()
        if response:
            if response['id'] and response['name']:
                print("[{}] {}".format(response['id'], response['name']))
            else:
                print('Not a valid JSON')
        else:
            print('No result')
    else:
        print('No result')
