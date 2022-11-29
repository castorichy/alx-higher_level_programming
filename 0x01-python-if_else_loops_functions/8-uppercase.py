#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) >= ord("a") and ord(ch) <= ord("z"):
            print(f"{chr(65 + ord(ch) - 97)}", end='')
        else:
            print(f"{ch:s}", end="")
