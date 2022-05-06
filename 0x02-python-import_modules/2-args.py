#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    # Index
    i = 0
if (len(sys.argv) - 1) == 1:
    print("{:d} argument:".format(len(sys.argv) - 1))
    while i < (len(sys.argv) - 1):
        print("{:d}: {}".format(i + 1, sys.argv[i + 1]))
        i = i + 1
# more of one arguments
elif (len(sys.argv) - 1) > 1:
    print("{:d} arguments:".format(len(sys.argv) - 1))
    while i < (len(sys.argv) - 1):
        print("{:d}: {}".format(i + 1, sys.argv[i + 1]))
        i = i + 1
else:
    print("{:d} arguments.".format(len(sys.argv) - 1))
