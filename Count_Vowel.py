# -*- coding: utf-8 -*-
"""
Module: Count_Vowel
Author: zen
Date: 14/7/2025 AD
"""


def main():
    '''Main Function'''
    a = int(input())
    count = 0
    characters = []
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for _ in range(a):
        characters.append(input(""))

    for ch in characters:
        if ch in vowel:
            count += 1

    print(count)

main()
