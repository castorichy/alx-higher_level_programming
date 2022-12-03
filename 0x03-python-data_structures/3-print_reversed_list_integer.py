#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for n in my_list[::-1]:
            print("{:d}".format(n))


if __name__ == "__main__":
    print_reverse_lis_integer()

