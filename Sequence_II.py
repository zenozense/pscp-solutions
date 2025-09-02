# -*- coding: utf-8 -*-
"""
Module: Sequence_II
Author: zen
Date: 4/8/2025 AD
"""


def main():
    '''Main Function'''
    square = int(input())

    matrix = []
    x = 0
    for i in range(square):
        row = []
        for j in range(square):
            row.append(x)
            x += 1
        matrix.append(row)

    for i in range(square):
        transposed_row = [str(matrix[j][i]) for j in range(square)]
        print(" ".join(transposed_row))

main()
