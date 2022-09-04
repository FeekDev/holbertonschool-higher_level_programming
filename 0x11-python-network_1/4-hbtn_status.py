#!/usr/bin/python3
import requests
'''
fetches the url and display
the body response
-------
packages requests
'''
if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status')

print("Body response:")
print("\t- type: {}".format(response.text.__class__))
print("\t- content: {}".format(response.text))
