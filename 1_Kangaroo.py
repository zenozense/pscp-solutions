# -*- coding: utf-8 -*-
"""
Module: 1_Kangaroo
Author: zen
Date: 11/9/2025 AD
"""

def main():
    """Main Function"""
    myList = []
    for _ in range(3):
        myList.append(int(input()))
    sorted(myList)
    result = max(myList[1] - myList[0], myList[2]-myList[1]) - 1
    print(result)

main()
