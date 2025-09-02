# -*- coding: utf-8 -*-
"""
Module: Elo
Author: zen
Date: 19/7/2025 AD
"""

def main():
    '''Main Function'''
    Ra = int(input())
    Rb = int(input())
    predictation = str(input())
    if predictation == 'A':
        Ea = 1/(1+10**((Rb - Ra)/400))
        print(f"{Ea:.2f}")
    else:
        Eb = 1 / (1 + 10 ** ((Ra - Rb) / 400))
        print(f"{Eb:.2f}")

main()
