# -*- coding: utf-8 -*-
"""
Module: R_Run_Length_Encoding
Author: zen
Date: 22/8/2025 AD
"""

def main():
    '''Main Function'''
    text = str(input())
    mydict = {}

    for char in text:
        mydict[char]= mydict.get(char, 0) + 1

    print(mydict)

main()
