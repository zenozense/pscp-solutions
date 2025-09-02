# -*- coding: utf-8 -*-
"""
Module: Ball
Author: zen
Date: 15/7/2025 AD
"""


def main():
    '''Main Function'''
    height = float(input())
    first_value = height
    counter = 0

    while height > 0.01:
        counter += 1
        height = height * (3/5)

    if first_value > 0.01:
        print(counter-1)
    else:
        print(0)

main()
