# -*- coding: utf-8 -*-
"""
Module: Calculator
Author: zen
Date: 14/7/2025 AD
"""


def main():
    '''Main Function'''
    x = int(input())
    text = ""
    if x == 1:
        print(1)
    else:
        for i in range(1, x+1,1):
            text += str(i)+"+"
        print(len(text))

main()
