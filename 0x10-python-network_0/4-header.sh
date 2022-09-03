#!/bin/bash
# sends a GET request to the URL and send a header variable
curl -s -H 'X-HolbertonSchool-User-Id: 98' -X GET "$1"
