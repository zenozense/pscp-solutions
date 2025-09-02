# -*- coding: utf-8 -*-
"""
Module: Frame
Author: zen
Date: 14/7/2025 AD
"""


def main():
    '''Main Function'''
    raw_text = str(input())
    length_star = len(raw_text)+2
    stars = "*" * length_star
    y = f"{stars}\n*{raw_text}*\n{stars}"
    print(y)

main()
