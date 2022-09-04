#!/usr/bin/python3
"""
This script make
------
sends a request to the URL
before the request obtain the header
"""
if __name__ == "__main__":
    import requests
    import sys

    response = requests.get(sys.argv[1])
    header = response.headers.get('X-Request-Id')
    print(header)
