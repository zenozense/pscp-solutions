# -*- coding: utf-8 -*-
"""
Module: Coke
Author: zen
Date: 5/8/2025 AD
"""

def main():
    '''Main Function'''
    a = int(input())  # ราคาปกติ
    b = int(input())  # จำนวนฝาที่ใช้แลก
    c = int(input())  # ราคาหลังใช้โปรโมชั่น
    d = int(input())  # จำนวนขวดที่ต้องการ

    price = 0
    cap = 0
    bought = 0

    while bought < d:
        if b > 0 and cap >= b and c < a: # pylint: disable=chained-comparison
            price += c
            cap = cap - b + 1
        else:
            price += a
            cap += 1
        bought += 1

    print(price)

main()
