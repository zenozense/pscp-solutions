# -*- coding: utf-8 -*-
"""
Module: 1_pig
Author: zen
Date: 19/9/2025 AD
"""

def main():
    """Main Function"""
    amount = int(input())
    summ = 0
    myList = input().split(" ")
    for i in range(0, amount+2, 2):
        summ += max(int(myList[i]), int(myList[i+1]))
        if i == amount+1:
        else:
            print(myList[i+1], end=" + ")
    print(summ)

main()
