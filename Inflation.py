# -*- coding: utf-8 -*-
"""
Module: Inflation
Author: zen
Date: 14/7/2025 AD
"""

def main():
    '''Main Function'''
    n = float(input().strip())
    k = int(input().strip())

    for _ in range(k):
        increase = n * 3.81 / 100

        increase = int(increase * 100) / 100
        n += increase

        print(f"{n:.2f}")

main()
