#!/usr/bin/python3
"""
This script make
------
takes in a URL and an email
sends a POST request to the passed URL
 the body of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    from urllib.request import urlopen, HTTPError, URLError
    from sys import argv
    try:
        with urlopen(argv[1]) as my_URL:
            print(my_URL.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: ', e.code)
