# -*- coding: utf-8 -*-
"""
Module: Palindrome
Author: zen
Date: 15/7/2025 AD
"""


def main():
    '''Main Function'''
    amount = int(input())
    text = str(input())
    text = text.replace(":", "")
    text_rev = text[::-1]
    counter = 0
    for j in range(amount):
        for i in text:
            if i == text_rev[counter%len(text)]:
                counter += 1
    print(text)

main()
