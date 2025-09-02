# -*- coding: utf-8 -*-
"""
Module: PongYa
Author: zen
Date: 5/8/2025 AD
"""

def main():
    '''Main Function'''
    x = int(input())
    print("PONG" if not x%3 or x % 10 == 3 else f"{x}")

main()
