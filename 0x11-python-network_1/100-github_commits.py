#!/usr/bin/python3


""" module to request """
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[1],
                                                                  sys.argv[2])
        login = requests.get(url).json()
        try:
            print(login)
        except KeyError:
            print('None')
    else:
        print('None')
