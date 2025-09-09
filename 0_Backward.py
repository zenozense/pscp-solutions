# -*- coding: utf-8 -*-
"""
Module: 0_Backward
Author: zen
Date: 9/9/2025 AD
"""

def main():
    """Main Function"""
    mylist = []
    while True:
        text = str(input())
        if text == "NULL":
            break
        mylist.append(text)

    mylist.reverse()
    for i in mylist:
        print(i)

main()
