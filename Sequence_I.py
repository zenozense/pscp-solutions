# -*- coding: utf-8 -*-
"""
Module: Sequence_I
Author: zen
Date: 4/8/2025 AD
"""


def main():
    '''Main Function'''
    row = int(input())
    col = int(input())
    x = 1

    for _ in range(row):
        line = []
        for _ in range(col):
            line.append(str(x))
            x += 1
        print(" ".join(line))

main()
