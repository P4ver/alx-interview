#!/usr/bin/python3
"""Rotate 2D Matrix,"""


def rotate_2d_matrix(matrix):
    """rotate two dimension matrix 90 degrees clockwise,"""
    q = len(matrix)
    for i in range(int(q / 2)):
        m = (q - i - 1)
        for j in range(i, m):
            x = (q - 1 - j)
            tmp = matrix[i][j]
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[m][x]
            matrix[m][x] = matrix[j][m]
            matrix[j][m] = tmp
