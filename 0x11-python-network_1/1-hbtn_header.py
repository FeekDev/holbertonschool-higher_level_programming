#!/usr/bin/python3
"""
This script make
------
sends a request to the URL
before the request obtain the header
"""
if __name__ == "__main__":
    from urllib.request import urlopen
    import sys
    with urlopen(sys.argv[1]) as response:
        header = response.getheader('X-Request-Id')
    print(header)
