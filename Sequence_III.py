# -*- coding: utf-8 -*-
"""
Module: Sequence_III
Author: zen
Date: 4/8/2025 AD
"""

def main():
    '''Main Function'''
    square = int(input())
    for i in range(2, square+2):
        line = []
        line.append(str(i))
        for j in range(i+1, square+i):
            line.append(str(j))
        print(" ".join(line))

main()
