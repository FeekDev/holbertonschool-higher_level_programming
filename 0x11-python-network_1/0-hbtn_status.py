#!/usr/bin/python3
from urllib.request import urlopen
'''
fetches the url and display
the body response
'''
if __name__ == "__main__":
    with urlopen("https://intranet.hbtn.io/status") as response:
        body = response.read()

print("Body response:$")
print(f"\t- type: {body.__class__}")
print(f"\t- content: {body}")
print(f"\t- utf8 content: {body.decode('utf-8')}")
