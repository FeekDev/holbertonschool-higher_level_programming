#!/usr/bin/python3
from urllib.request import urlopen
'''
fetches the url and display
the body response
'''
if __name__ == "__main__":
    with urlopen("https://intranet.hbtn.io/status") as response:
        body = response.read()

print("Body response:")
print("\t- type: {}".format(body.__class__))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode('utf-8')))
