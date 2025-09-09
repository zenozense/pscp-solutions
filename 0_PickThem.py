# -*- coding: utf-8 -*-
"""
Module: 0_PickThem
Author: zen
Date: 9/9/2025 AD
"""
import json

def main():
    """Main Function"""
    myList = json.loads(str(input()))
    not_even_count = 0

    for _, value in enumerate(myList):
        if value % 2:
            not_even_count += 1

    if not_even_count == len(myList):
        print("Nope")
    else:
        for j in myList:
            if not j % 2:
                print(j)

main()
