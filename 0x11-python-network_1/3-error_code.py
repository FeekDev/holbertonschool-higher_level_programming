#!/usr/bin/python3
"""
This script make
------
takes in a URL and an email
sends a POST request to the passed URL
 the body of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.request import HTTPError, URLError
    from sys import argv

    my_URL = Request(argv[1])
    try:
        with urlopen(my_URL) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code:', e.code)
