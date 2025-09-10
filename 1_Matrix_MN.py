# -*- coding: utf-8 -*-
"""
Module: 1_Matrix_MN
Author: zen
Date: 10/9/2025 AD
"""

def main():
    """Main Function"""
    m = int(input())
    n = int(input())
    myList = []

    for _ in range(m*n):
        myList.append(int(input()))

    for j in range(m):
        for k in range(n):
            if k == n-1:
                print(myList[j*n+k], end="")
            else:
                print(myList[j*n+k], end=" ")
        print("")

main()
