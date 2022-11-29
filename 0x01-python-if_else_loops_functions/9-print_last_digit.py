#!/usr/bin/python3
def print_last_digit(number):
    number =  "{:d}".format(int(repr(number)[-1]))
    print(number)
    return number
