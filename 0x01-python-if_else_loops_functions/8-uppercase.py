#!/usr/bin/python3
# Prototype
def uppercase(str):
    for i in str:
        c = ord(i)
        if c <= 122 and c >= 97:
            c = chr(c - 32)
        else:
            c = chr(c)
        print(f"{c}", end="")
    print()
