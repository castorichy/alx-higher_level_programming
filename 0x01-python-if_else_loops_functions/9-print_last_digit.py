#!/usr/bin/python3
def print_last_digit(number):
    return "{:d}".format(int(repr(number)[-1]))
