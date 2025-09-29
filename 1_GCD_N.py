# -*- coding: utf-8 -*-
"""
Module: 1_GCD_N
Author: zen
Date: 10/9/2025 AD
"""
import math

def main():
    """Main Function"""
    N = int(input())
    numbers = []
    for _ in range(N):
        numbers.append(int(input()))

    if len(numbers) != N:
        return

    gcd_value = numbers[0]
    for i in range(1, N):
        gcd_value = math.gcd(gcd_value, numbers[i])
    print(gcd_value)
main()
