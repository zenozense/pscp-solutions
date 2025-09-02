# -*- coding: utf-8 -*-
"""
Module: Turnstile
Author: zen
Date: 4/8/2025 AD
"""


def main():
    '''Main Function'''
    x = True
    state = True # Lock
    count = 0

    while x:
        logs = str(input())
        if logs == "END":
            print(count)
            x = False
        elif logs == "C":
            state = False
        elif logs == "P":
            if state is True:
                continue
            count += 1
            state = True
main()
