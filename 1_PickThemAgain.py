# -*- coding: utf-8 -*-
"""
Module: 1_PickThemAgain
Author: zen
Date: 10/9/2025 AD
"""

def main():
    """Main Function"""
    x = input().split()
    x.reverse()
    counter = 0
    for i in x:
        if not int(i) % 3 or not int(i) % 5:
            print(i)
        else:
            counter += 1
    if counter == len(x):
        print("Nope")

main()
