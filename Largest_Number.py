# -*- coding: utf-8 -*-
"""
Module: Largest_Number
Author: zen
Date: 19/7/2025 AD
"""

def main():
    """Docstring"""

    a = input()
    b = input()
    c = input()

    if b + a > a + b:
        a, b = b, a
    if c + a > a + c:
        a, c = c, a
    if c + b > b + c:
        b, c = c, b

    result = a + b + c
    if result[0] == '0':
        print('0')
    else:
        print(result)

main()
