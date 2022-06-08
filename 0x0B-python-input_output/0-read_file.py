#!/usr/bin/python3
"""
reads a text file and prints it to stdout
"""


def read_file(filename=""):
    """
    statment in mode read
    """
    with open('my_file_0.txt', encoding="UTF8") as f:
        read_file = f.read()
    print(read_file)
