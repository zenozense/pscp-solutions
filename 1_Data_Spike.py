# -*- coding: utf-8 -*-
"""
Module: 1_Data_Spike
Author: zen
Date: 9/9/2025 AD
"""

def main():
    """Main Function"""
    maxx = 0
    for _ in range(8):
        x = int(input())
        if x > maxx:
            maxx = x
        else:
            continue

    print(maxx)

main()
