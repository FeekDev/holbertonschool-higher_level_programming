#!/usr/bin/python3
import sys

if (len(sys.argv) - 1) > 0 and (len(sys.argv) - 1) <= 1:
    print("{:d} arguments:".format(len(sys.argv) - 1))
    print("1: {}".format(sys.argv[1]))
elif (len(sys.argv) - 1) > 1:
    print("{:d} arguments:".format(len(sys.argv) - 1))
    print("1: {}".format(sys.argv[1]))
    print("2: {}".format(sys.argv[2]))
    print("3: {}".format(sys.argv[3]))
    print("4: {}".format(sys.argv[4]))
    print("5: {}".format(sys.argv[5]))
    print("6: {}".format(sys.argv[6]))
else:
    print("{:d} arguments.".format(len(sys.argv) - 1))
