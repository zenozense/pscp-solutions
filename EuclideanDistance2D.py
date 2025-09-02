# -*- coding: utf-8 -*-
"""
Module: EuclideanDistance2D
Author: zen
Date: 14/7/2025 AD
"""
import math

def main():
    '''Main Function'''
    q1 = float(input())
    q2 = float(input())
    p1 = float(input())
    p2 = float(input())
    y = math.sqrt(((q1-p1)**2)+((q2-p2)**2))
    print(y)

main()
