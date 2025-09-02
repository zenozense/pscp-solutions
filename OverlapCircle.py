# -*- coding: utf-8 -*-
"""
Module: OverlapCircle
Author: zen
Date: 19/7/2025 AD
"""

import math

def main():
    '''Main Function'''
    x1 = float(input())
    y1 = float(input())
    r1 = float(input())
    x2 = float(input())
    y2 = float(input())
    r2 = float(input())

    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    if d < r1 + r2 or d == r1 + r2:
        print('overlapping')
    elif d > r1 + r2:
        print('no overlapping')

main()
