# -*- coding: utf-8 -*-
"""
Module: Orange
Author: zen
Date: 11/8/2025 AD
"""


def main():
    '''Main Function'''
    floor = int(input())
    sell = int(input())
    sum_orange = 0
    final = 0
    floorl = []
    for i in range(floor):
        sum_orange += (floor-i)**2
        floorl.append(sum_orange)
    sum_orange = floorl[-1] - sell

    for j, _ in enumerate(floorl):
        if sum_orange > floorl[j]:
            final = j+2
        elif sum_orange <= 0:
            final = 0
        elif sum_orange <= floorl[0]:
            final = 1
    print(final)

main()
