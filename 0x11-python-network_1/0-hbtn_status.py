#!/usr/bin/python3



""" module urllib """
import urllib.request



""""
	script that fetches an url
"""


if __name__ == "__main__":

    with urllib.request.urlopen('https://intranet.hbtn.io/status')  as response:
        data = response.read() 

    if data:
        print("Body response:")
        print("\t-type: {}".format(type(response.read())))
        print("\t-content: {}".format(data))
        print("\t-utf8 content: {}".format(data.decode('utf-8')))
