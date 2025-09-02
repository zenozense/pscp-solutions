# -*- coding: utf-8 -*-
"""
Module: isPrime_large
Author: zen
Date: 5/8/2025 AD
"""

def is_prime(x):
    '''check is prime or not'''
    if x < 2:
        return False
    if x == 2:
        return True
    if not x % 2:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if not x % i:
            return False
    return True

def main():
    '''Main Function'''
    x = int(input())
    if is_prime(x):
        print("YES")
    else:
        print("NO")

main()
