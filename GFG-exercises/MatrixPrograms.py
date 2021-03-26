from math import prod


def add_matrices(matrix1, matrix2):
    combined = zip(matrix1, matrix2)
    combined = [item for item in combined]
    converted = [list(zip(zipped1, zipped2)) for (zipped1, zipped2) in combined]
    added = [[sum(list(tuple)) for tuple in list(zip(zipped1, zipped2))] for (zipped1, zipped2) in combined]
    return added


def add_matrices_revised(matrix1, matrix2):
    result = [list(map(sum, zip(*tuple))) for tuple in zip(matrix1, matrix2)]
    return result


def multiply_matrices(matrix1, matrix2):
    return [list(map(prod, zip(*tuple))) for tuple in zip(matrix1, matrix2)]


if __name__ == '__main__':
    print(add_matrices([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]))
    print(add_matrices_revised([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]))
    print(multiply_matrices([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]))