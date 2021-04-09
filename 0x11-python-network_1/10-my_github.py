#!/usr/bin/python3


""" module to request """
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 3:
        username = sys.argv[1]
        token = sys.argv[2]
        login = requests.get('https://api.github.com/user',
                             auth=(username, token)).json()
        try:
            print(login['id'])
        except KeyError:
            print('None')
    else:
        print('None')
