# -*- coding: utf-8 -*-
"""
Module: 0_Ascending_Sort
Author: zen
Date: 9/9/2025 AD
"""

def main():
    """Main Function"""
    ranged = int(input())
    mylist = []
    for _ in range(ranged):
        mylist.append(int(input()))
    mylist.sort()

    for j in range(ranged):
        print(mylist[j])

main()
