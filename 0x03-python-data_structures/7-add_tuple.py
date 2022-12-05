#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    b = [0, 0]
    for index, value in enumerate(tuple_a):
        if index < 2:
            a[index] = value[index]
    for index, value in enumerate(tuple_b):
        if index < 2:
            b[index] = value[index]
    sum_a = a[1] + b[1]
    sum_b = a[2] + b[2]
    return sum_a, sum_b
