#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for num in my_list:
        print("{}".format(num))


print_list_integer([3, 4, 5, 7, 2, 33])
if __name__ == "__main__":
    print_list_integer(my_list=[])
