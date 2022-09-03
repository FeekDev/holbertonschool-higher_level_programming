#!/bin/bash
# sends a POST request add two variables
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
