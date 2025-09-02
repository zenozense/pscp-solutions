# -*- coding: utf-8 -*-
"""
Module: Top_Test_Score
Author: zen
Date: 14/7/2025 AD
"""

def main():
    '''Main Function'''
    students = int(input())
    top_score = -1
    count_top = 0

    i = 0
    while i < students:
        score = int(input())

        if score > top_score:
            top_score = score
            count_top = 1
        elif score == top_score:
            count_top += 1

        i += 1

    print(top_score)
    print(count_top)

main()
