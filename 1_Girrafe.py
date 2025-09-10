# -*- coding: utf-8 -*-
"""
Module: 1_Girrafe
Author: zen
Date: 10/9/2025 AD
"""

def main():
    """Main Function"""
    amount = int(input())
    myList = [int(input()) for _ in range(amount)]
    counter = 0

    if amount == 1:
        print(1)
        return

    for j in range(amount):
        current = myList[j]

        if not j:
            if current > myList[j+1]:
                counter += 1
        elif j == amount - 1:
            if current > myList[j-1]:
                counter += 1

        else:
            if current > myList[j-1] and current > myList[j+1]:
                counter += 1

    print(counter)

main()
