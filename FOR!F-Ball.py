# -*- coding: utf-8 -*-
"""
Module: FOR!F-Ball
Author: zen
Date: 4/8/2025 AD
"""

def main():
    '''Main Function'''
    x = str(input())
    store = 1
    for char in x:
        if char == "A" and store == 1:
            store = 2
        elif char == "A" and store == 2:
            store = 1
        elif char == "B" and store == 2:
            store = 3
        elif char == "B" and store == 3:
            store = 2
        elif char == "C" and store == 1:
            store = 3
        elif char == "C" and store == 3:
            store = 1
    print(store)
main()
