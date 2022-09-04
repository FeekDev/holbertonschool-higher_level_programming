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

    response = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(response.text)
