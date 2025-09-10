# -*- coding: utf-8 -*-
"""
Module: 0_Bubble_Tea
Author: zen
Date: 10/9/2025 AD
"""

def main():
    """Main Function"""
    kaimook_type , kaimook_amount = input().split()
    tea_type , sweet_level , tea_amount = map(str, input().split())

    kaimook_cal = {
        "H": 5,
        "O": 3,
        "J": 2
    }

    tea_cal = {
        "R": {1: 12, 2: 18, 3: 25},
        "T": {1: 15, 2: 20, 3: 30},
        "M": {1: 10, 2: 15, 3: 20}
    }

    total_cal = 0

    if kaimook_type in kaimook_cal:
        total_cal += kaimook_cal[kaimook_type] * int(kaimook_amount)

    if tea_type in tea_cal and int(sweet_level) in tea_cal[tea_type]:
        total_cal += tea_cal[tea_type][int(sweet_level)] * int(tea_amount)

    print(total_cal)

main()
