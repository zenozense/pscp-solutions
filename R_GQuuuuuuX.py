# -*- coding: utf-8 -*-
"""
Module: GQuuuuuuX
Author: zen
Date: 22/8/2025 AD
"""


def main():
    '''Main Function'''
    text = str(input().lower())

    result = ""
    prev = ""

    for char in text:
        if char == "u" and prev == "u":
            continue
        result += char
        prev = char

    if "gqux" in result:
        max_count = 0
        count = 0

        for i in range(len(text)-1):
            if text[i] == 'u':
                count += 1
                if text[i+1] == 'x':
                    if count > max_count:
                        max_count = count
            else:
                count = 0
        print(max_count)
    else:
        print("None")

main()
