# -*- coding: utf-8 -*-
"""
Module: 113
Author: zen
Date: 5/8/2025 AD
"""

def main():
    '''Main Function'''
    text = str(input())
    store = "113"
    for _ in range(10):
        text = text.replace(store, "")
    print(text)

main()
