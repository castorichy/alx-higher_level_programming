#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        new_matrix = []
        try:
            for row in matrix:
                new_matrix.append(list(map(lambda x: x*x, row)))
            return new_matrix
        except TypeError:
            return None


if __name__ == "__main__":
    square_matrix_simple()
