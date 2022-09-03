#!/bin/bash
# sends a GET request to the URL and send a header variable
curl -H 'X-HolbertonSchool-User-Id: 98' -X GET "$1"
