#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for index, lst in row:
                print("{:d}".format(lst), end=' ')
                if index < len(row):
                    print("{}".format(" "), end='')
            print()
