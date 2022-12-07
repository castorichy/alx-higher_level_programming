#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1:
        if set_2:
            lis = list(set_1 & set_2)
            return lis


if __name__ == "__main__":
    common_elements()
