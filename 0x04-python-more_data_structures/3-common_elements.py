#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 and set_2:
        lis = list(set_1 & set_2)
        if not lis:
            return None
        else:
            return lis


if __name__ == "__main__":
    common_elements()
