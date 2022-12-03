#!/usr/bin/python3
if __name__ == "__main__":
    element_at = __import__ ("2-replace_in_list").replace_in_list
    my = [12, 45, 65, 66, 5, 44, 33, 3]
    idx = -1
    elem = 44
    print(element_at(my, idx, elem))
