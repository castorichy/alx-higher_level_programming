#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    a = 10
    b = 5
    print("{} + {} = {}".fomat(a, b, add(a, b)))
    print("{} - {} = {}".fomat(a, b, sub(a, b)))
    print("{} * {} = {}".fomat(a, b, mul(a, b)))
    print("{} / {} = {}".fomat(a, b, div(a, b)))
