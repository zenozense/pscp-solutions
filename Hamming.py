# -*- coding: utf-8 -*-
"""
Module: Hamming
Author: zen
Date: 5/8/2025 AD
"""

def main():
    '''Main Function'''
    text = str(input())
    text2 = str(input())
    counter = 0
    for ch1, ch2 in zip(text, text2):
        if ch1 != ch2:
            counter += 1
    print(counter)

main()
