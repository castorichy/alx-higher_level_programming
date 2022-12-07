#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is not None:
        my_list = set(my_list)
        sum = 0
        for elem in my_list:
            sum += elem
        return sum


if __name__ == "__main__":
    uniq_add()
