#!/usr/bin/python3

# Function to compute the sqaure value of all integers of a matrix
def sqaure_matrix_simple(matrix=[]):
    result = matrix.copy()

    for i in range(len(matrix)):
        result[i] = list(map(lambda x: x**2, matrix[i]))

    return (result)
