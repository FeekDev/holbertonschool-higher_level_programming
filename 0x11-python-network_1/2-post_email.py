#!/usr/bin/python3
"""
This script make
------
takes in a URL and an email
sends a POST request to the passed URL
 the body of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    from urllib.request import urlopen
    from urllib.parse import urlencode
    from sys import argv
    data = urlencode({'email': argv[2]})
    data = data.encode('utf-8')
    with urlopen(argv[1], data) as post:
        print(post.read().decode('utf-8'))
