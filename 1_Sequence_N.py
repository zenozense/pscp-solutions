# -*- coding: utf-8 -*-
"""
Module: 1_Sequence_N
Author: zen
Date: 9/9/2025 AD
"""

def main():
    """Main Function"""
    mn = int(input())
    for i in range(mn):
        for j in range(mn):
            if not i or i in (0, mn-1):
                if not j or j in (0, mn-1):
                    print("*", end="")
                else:
                    print(" ", end="")
            else:
                if not j or j in (0, mn-1):
                    print("*", end="")
                elif j == 1 and i == 1:
                    print("*", end="")
                elif j == mn-2 and i == mn-2:
                    print("*", end="")
                elif j == i and i == j:
                    print("*", end="")
                else:
                    print(" ", end="")
        print("")

main()
