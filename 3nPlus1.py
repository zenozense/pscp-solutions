# -*- coding: utf-8 -*-
"""
Module: 3nPlus1
Author: zen
Date: 4/8/2025 AD
"""

def main():
    '''Main Function'''
    while True:
        n = int(input())
        if not n:
            break

        store = 1

        while n != 1:
            if not n % 2:
                n = n/2
                store += 1
            else:
                n = (n*3)+1
                store += 1
        print(store)

main()
