# -*- coding: utf-8 -*-
"""
Module: 1_LineSorting
Author: zen
Date: 10/9/2025 AD
"""

def main():
    """Main Function"""
    amount = int(input())
    myList = []
    for _ in range(amount):
        myList.append(str(input()))
    myList.sort(key=len)

    for j in myList:
        print(j)
main()
