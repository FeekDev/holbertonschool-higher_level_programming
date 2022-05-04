#!/usr/bin/python3
# range an iteration
for i in range(0, 10):
    # i is the first number
    for n in range((i + 1), 10):
        # n is the second number
        if i == 8 and n == 9:
            print(f"{i}{n}")
        else:
            print(f"{i}{n}", end=", ")
