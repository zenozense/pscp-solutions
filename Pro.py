# -*- coding: utf-8 -*-
"""
Module: Pro
Author: zen
Date: 19/7/2025 AD
"""


def main():
    '''Main Function'''
    x = int(input()) # จำนวนคนที่มา (Template)
    y = int(input()) # จำนวนชุดคนจ่าย (Template)
    raw_price = int(input())
    z = int(input()) # จำนวนคนที่มาจริง ๆ
    counter = 0
    counter_sep = 0

    counter += z//x
    counter_sep += z % x

    print(counter*(raw_price*y) + raw_price*counter_sep)

main()
