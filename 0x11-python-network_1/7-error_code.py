#!/usr/bin/python3
"""
This script make
------
takes in a URL and an email
sends a POST request to the passed URL
 the body of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    import requests
    import sys

    bad_code = requests.get(sys.argv[1])
    if bad_code.status_code >= 400:
        print("Error code: {}".format(bad_code.status_code))
    else:
        print(bad_code.text)
