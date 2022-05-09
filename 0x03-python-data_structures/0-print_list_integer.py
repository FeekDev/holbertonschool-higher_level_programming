#!/usr/bin/python3

def print_list_integer(my_list=[]):
    # allow the list and optional lenght
    randlist = my_list
    # this loop travel the list and print
    for i in randlist:
        print(f"{i}")


if __name__ == "__main__":
    print_list_integer(my_list=[])
