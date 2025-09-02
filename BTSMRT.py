# -*- coding: utf-8 -*-
"""
Module: BTSMRT
Author: zen
Date: 19/7/2025 AD
"""

def main():
    """Main Function"""
    day = input().strip()
    year = float(input())
    height = float(input())

    if year < 14 and height < 90:
        print("FREE")
    else:
        if day == "Children Day":
            if year < 14 and height <= 140:
                print("FREE")
            else:
                print("PAY")
        elif day == "Senior Day":
            if year >= 60:
                print("FREE")
            else:
                print("PAY")
        else:
            print("PAY")

main()
