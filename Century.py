# -*- coding: utf-8 -*-
"""
Module: Century
Author: zen
Date: 5/8/2025 AD
"""

def main():
    '''Main Function'''
    amount = int(input())
    for _ in range(amount):
        era, number = str(input()).split(" ")
        number = int(number)
        era = era.upper()

        if era == "B.E.":
            number -= 543

        if number <= 0:
            print("ERROR")
        elif not number % 100:
            print(number // 100)
        else:
            print((number // 100) + 1)

main()
