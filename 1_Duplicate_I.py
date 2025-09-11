# -*- coding: utf-8 -*-
"""
Module: 1_Duplicate_I
Author: zen
Date: 11/9/2025 AD
"""

def main():
    """Main Function"""
    m = int(input())
    n = int(input())
    m_member = {int(input()) for _ in range(m)}
    n_member = {int(input()) for _ in range(n)}
    x = m_member.intersection(n_member)
    x = sorted(x, reverse=True)

    if not x:
        print("Nope")
    else:
        for value in x:
            print(value)

main()
