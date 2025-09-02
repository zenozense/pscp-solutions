# -*- coding: utf-8 -*-
"""
Module: Safe_Password
Author: zen
Date: 14/7/2025 AD
"""


def main():
    '''Main Function'''
    alphabet = str(input())
    num = int(input())
    if alphabet == "H" and num != 4567:
        print("safe locked - change digit")
    elif num == 4567 and alphabet != "H":
        print("safe locked - change char")
    elif num == 4567 and alphabet == "H":
        print("safe unlocked")
    else:
        print("safe locked")

main()
