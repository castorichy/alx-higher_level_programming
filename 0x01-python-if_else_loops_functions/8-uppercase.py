#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) >= ord("a") and ord(ch) <= ord("z"):
            print("{}".format(chr(65 + ord(ch) - 97)), end='')
        else:
            print("{:s}".format(ch), end="")
    print("")
