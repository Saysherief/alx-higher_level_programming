#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    function that computes the square value of all integers of a matrix
    """
    answer = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            answer[i][j] = matrix[i][j] ** 2
    return answer
