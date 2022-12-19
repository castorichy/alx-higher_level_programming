#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list:
        try:
            y = 0
            for idx in range(x):
                print("{}".format(my_list[idx]), end="")
                y += 1
            return y
        except IndexError:
            return y


if __name__ == "__main__":
    safe_print_list()
