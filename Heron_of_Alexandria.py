# -*- coding: utf-8 -*-
"""
Module: Heron_of_Alexandria
Author: zen
Date: 14/7/2025 AD
"""

import math

def main():
    '''Main Function'''
    a = float(input())
    b = float(input())
    c = float(input())
    s = (a + b + c)/2
    Area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"{Area:.3f}")

main()
