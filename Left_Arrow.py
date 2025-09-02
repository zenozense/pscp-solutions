# -*- coding: utf-8 -*-
"""
Module: Left_Arrow
Author: zen
Date: 4/8/2025 AD
"""

def main():
    '''Main Function'''
    n = int(input())
    m = int(input())
    divvalue = int(0 - ((m-1)/2))
    for i in range(divvalue, abs(divvalue)+1, 1):
        print(" "*abs(i)+"*"*n)

main()
