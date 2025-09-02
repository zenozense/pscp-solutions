# -*- coding: utf-8 -*-
"""
Module: SquidGame3_Tug_of_War
Author: zen
Date: 15/7/2025 AD
"""


def main():
    '''Main Function'''
    TeamA_Sum = 0
    TeamB_Sum = 0
    count = 0
    for _ in range(20):
        count += 1
        power = int(input())
        if count <= 10:
            TeamA_Sum += power
        else:
            TeamB_Sum += power

    if TeamA_Sum == TeamB_Sum:
        print("AB")
    elif TeamA_Sum < TeamB_Sum:
        print("A")
    else:
        print("B")

main()
