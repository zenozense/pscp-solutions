# -*- coding: utf-8 -*-
"""
Module: Key
Author: zen
Date: 5/8/2025 AD
"""

def main():
    x = input()
    summation = sum(int(i) for i in x)
    last3 = int(x[-3:]) * 10
    total = summation + last3

    if total > 9999:
        total %= 10000
    if total < 1000:
        total += 1000

    print(total)

main()
