# -*- coding: utf-8 -*-
"""
Module: 1_MissingNumber
Author: zen
Date: 10/9/2025 AD
"""

def main():
    """Main Function"""
    myList = []
    noted = []
    while True:
        x = int(input())
        if not x:
            break
        myList.append(x)

    for i in range(1, max(myList) + 1):
        if i not in myList:
            noted.append(i)
        else:
            continue

    noted = sorted(noted)
    print('\n'.join(str(i) for i in noted))
    
main()
