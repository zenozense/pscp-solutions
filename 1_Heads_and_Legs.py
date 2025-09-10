# -*- coding: utf-8 -*-
"""
Module: 1_Heads_and_Legs
Author: zen
Date: 10/9/2025 AD
"""

def main():
    """Main Function"""
    total_animals = int(input())
    total_legs = int(input())

    rabbit = (total_legs - 2*total_animals) // 2
    bird = (4*total_animals - total_legs) // 2

    if rabbit < 0 or bird < 0 or 4*rabbit + 2*bird != total_legs or rabbit + bird != total_animals:
        print("Impossible")
    else:
        print(rabbit, bird)

main()
