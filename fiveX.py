# -*- coding: utf-8 -*-
"""
Module: fiveX
Author: zen
Date: 5/8/2025 AD
"""


def main():
    '''Main Function'''
    number = int(input())
    for i in range(1, number+1):
        if not i % 5:
            print("X", end="")
        else:
            print("*", end="")

main()
