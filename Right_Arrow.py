# -*- coding: utf-8 -*-
"""
Module: Right_Arrow
Author: zen
Date: 4/8/2025 AD
"""

def main():
    '''Main Function'''
    n = int(input())
    m = int(input())
    index = 0
    direction = 1
    space = list(range(int((m - 1) / 2)+1))
    for _ in range(m):
        print(" "*space[index]+"*"*n)
        index += direction
        if index in (len(space)-1, 0):
            direction *= -1

main()
