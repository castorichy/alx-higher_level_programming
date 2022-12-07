#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1:
        if set_2:
            lis = list(set_1 - set_2)
            if lis is not None:
                return lis


if __name__ == "__main__":
    only_diff_element()