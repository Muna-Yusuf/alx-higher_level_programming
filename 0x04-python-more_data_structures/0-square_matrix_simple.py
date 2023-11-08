#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for x in matrix:
        new_list.append([i ** 2 for i in x])
    return (new_list)
