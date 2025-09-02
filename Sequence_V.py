# -*- coding: utf-8 -*-
"""
Module: Sequence_V
Author: zen
Date: 5/8/2025 AD
"""

def main():
    '''Main Function'''
    x = int(input())
    for i in range(x, 0, -1):
        if i % 7 == 0:
            print(" ")
        print(i, end=" ")

main()
