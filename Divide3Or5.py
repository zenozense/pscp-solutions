# -*- coding: utf-8 -*-
"""
Module: Divide3Or5
Author: zen
Date: 4/8/2025 AD
"""

def main():
    '''Main Function'''
    x = int(input())
    summ = 0
    for i in range(1, x+1):
        if not i % 3:
            summ += i
        elif not i % 5:
            summ += i
        else:
            continue
    print(summ)

main()
