#!/bin/bash
#
curl -Lsi -X OPTIONS "$1" | grep Allow | cut -c 8-
