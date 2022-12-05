#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(len(matrix)):
            for lst in matrix[i]:
                print("{:d}".format(lst), end=' ')
            print()
