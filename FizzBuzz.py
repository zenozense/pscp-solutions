# -*- coding: utf-8 -*-
"""
Module: FizzBuzz
Author: zen
Date: 14/7/2025 AD
"""


def main():
    '''Main Function'''
    num = int(input())

    for i in range(1, num+1, 1):
        if not i % 3 and not i % 5:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)

main()
