#!/usr/bin/python3
if __name__ == "__main__":
    element_at = __import__ ("3-print_reversed_list_integer").print_reversed_list_integer
    my = [9, 12, 45, 65, 66, 5, 44, 33, 3]
    idx = -1
    elem = 44
    print(element_at(my))
