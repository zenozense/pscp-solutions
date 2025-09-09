# -*- coding: utf-8 -*-
"""
Module: 0_Grocery
Author: zen
Date: 9/9/2025 AD
"""


def main():
    """Main Function"""
    total_carrot, total_cabbage, total_tomato = map(int, input().split(" "))

    print(total_carrot*10 + total_cabbage*25 + total_tomato*3)

main()
