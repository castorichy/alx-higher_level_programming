#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        y = 0
        for idx in range(x):
            print("{}".format(my_list[idx]), end="")
            y += 1
        print()
        return y
    except IndexError:
        print()
        return y


if __name__ == "__main__":
    safe_print_list()