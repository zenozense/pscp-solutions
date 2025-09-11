# -*- coding: utf-8 -*-
"""
Module: 1_Easy_Histogram
Author: zen
Date: 10/9/2025 AD
"""

def main():
    """Main Function"""
    text = input().replace(" ", "")
    result = {}

    for ch in text:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1

    for ch in sorted(result, key=lambda x: (x.lower(), x.isupper())):
        print(f"{ch} = {result[ch]}")

main()
