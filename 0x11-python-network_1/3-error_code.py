#!/usr/bin/python3



""" module urllib """
import urllib.request
import urllib.error
import sys



""""
	script that fetches an url
"""


if __name__ == "__main__":

    if len(sys.argv) == 2:
            try:
                with urllib.request.urlopen(sys.argv[1])  as response:
                    data = response.read() 
                    print("{}".format(data.decode('utf-8')))
            except urllib.error.HTTPError as e:
                if e.code == 401:
                    print('Error code: 401')
                if e.code == 404:
                    print('Error code: 404')
                if e.code == 500:
                    print('Error code: 500')
