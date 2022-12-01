#!/usr/bin/python3
import calculator_1 as cal

if __name__ == '__main__':
    a = 10
    b = 5
    print("{} + {} = {}".fomat(a, b, cal.add(a, b)))
    print("{} - {} = {}".fomat(a, b, cal.sub(a, b)))
    print("{} * {} = {}".fomat(a, b, cal.mul(a, b)))
    print("{} / {} = {}".fomat(a, b, cal.div(a, b)))
