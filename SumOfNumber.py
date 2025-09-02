# -*- coding: utf-8 -*-
"""
Module: SumOfNumber
Author: zen
Date: 4/8/2025 AD
"""

def main():
    '''Main Function'''
    try:
        target = int(input())
        summation = target
    except (ValueError, EOFError):
        target = 0
        summation = target
    while True:
        try:
            x = int(input())
            if x == -1:
                break
            summation += x
        except EOFError:
            break
        except ValueError:
            pass
    print(summation-target)
main()
