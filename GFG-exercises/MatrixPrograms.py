from math import prod
from itertools import chain
from functools import reduce
from operator import mul
import numpy as np


def add_two_matrices(matrix1, matrix2):
    combined = zip(matrix1, matrix2)
    combined = [item for item in combined]
    added = [[sum(list(tup)) for tup in list(zip(zipped1, zipped2))] for (zipped1, zipped2) in combined]
    return added


def add_matrices_revised(matrix1, matrix2):
    result = [list(map(sum, zip(*tup))) for tup in zip(matrix1, matrix2)]
    return result


def multiply_matrices(matrix1, matrix2):
    return [list(map(prod, zip(*tup))) for tup in zip(matrix1, matrix2)]


def dot_product(matrix1, matrix2):
    transponed_m2 = list(map(list, zip(*matrix2)))
    product = [list(map(prod, zip(*tup))) for tup in zip(matrix1, transponed_m2)]
    return product


def multiply_all_elements(matrix):
    elements = list(chain(*matrix))
    product = reduce(mul, elements)
    return product


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def add_matrices(matrix1, matrix2):
    return np.add(matrix1, matrix2)


def subtract_matrices(matrix1, matrix2):
    return np.subtract(matrix1, matrix2)


def add_multiple_matrices(*matrices):
    return reduce(np.add, matrices)


def subtract_multiple_matrices(*matrices):
    return reduce(np.subtract, matrices)


def create_matrix(size):
    return [[y for y in range(size*x, x*size+size+1)] for x in range(size)]


def get_kth_column(matrix, k):
    return [row[k] for row in matrix]


def vertical_concat(matrix):
    return ["".join(row) for row in zip(*matrix)]


if __name__ == '__main__':
    # print(add_two_matrices([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]))
    # print(add_matrices_revised([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]))
    # print(multiply_matrices([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]))
    # print(dot_product([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]))
    # print(multiply_all_elements([[1, 4, 5], [7, 3], [4], [46, 7, 3]]))
    # print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # print(add_matrices([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]))
    # print(subtract_matrices([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]))
    print(add_multiple_matrices([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                                [[9, 8, 7], [6, 5, 4], [3, 2, 1]],
                                [[9, 8, 7], [6, 5, 4], [3, 2, 1]]))
    print(subtract_multiple_matrices([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                                     [[9, 8, 7], [6, 5, 4], [3, 2, 1]],
                                     [[9, 8, 7], [6, 5, 4], [3, 2, 1]]))
    print(create_matrix(5))
    print(get_kth_column([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2))
    print(vertical_concat([["this", "is", "test"], ["My", "name", "sander"], ["Who", "are", "you"]]))
