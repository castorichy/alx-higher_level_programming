#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    y = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
        except (ValueError, TypeError):
            y -= 1
            continue
    print()
    return (idx + 1) + y
