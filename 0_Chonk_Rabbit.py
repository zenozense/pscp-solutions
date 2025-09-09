# -*- coding: utf-8 -*-
"""
Module: 0_Chonk_Rabbit
Author: zen
Date: 9/9/2025 AD
"""

def main():
    """Main Function"""
    amount = int(input())
    NameCol = []
    WeightCol = []
    overweight = 0
    for _ in range(amount):
        name , weight = input().split(" ")
        if int(weight) > 15:
            overweight += 1
        NameCol.append(name)
        WeightCol.append(weight)

    print(overweight)
    print(NameCol[WeightCol.index(max(WeightCol))], max(WeightCol))

main()
