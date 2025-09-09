# -*- coding: utf-8 -*-
"""
Module: 999_Pairing
Author: zen
Date: 9/9/2025 AD
"""


def main():
    """Main Function"""
    length = int(input())
    a = str(input())
    b = str(input())
    summ = 0

    for i in range(length):
        if int(a[i]) + int(b[i]) == 9:
            summ += 1
        else:
            continue

    if summ == length:
        print("YES")
    else:
        print(f"NO {length-summ}")

main()
