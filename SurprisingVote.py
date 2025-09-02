# -*- coding: utf-8 -*-
"""
Module: SurprisingVote
Author: zen
Date: 15/7/2025 AD
"""

def main():
    '''Main Function'''
    summation = float(input())
    first = float(input())
    third = 0
    if first*2 < summation:
        third = summation - first*2
    if first - third > 2:
        print("Surprising")
    else:
        print("Not surprising")

main()
