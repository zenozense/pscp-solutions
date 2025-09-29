# -*- coding: utf-8 -*-
"""
Module: 1_RuleofThree
Author: zen
Date: 18/9/2025 AD
"""

def main():
    """Main Function"""
    amount_compare = int(input())
    size = []
    price = []
    ratio = []
    for i in range(amount_compare):
        size.append(float(input()))
        price.append(float(input()))
        ratio.append(price[i]/(size[i]))

    min_ratio = max(ratio)
    candidates = [i for i, r in enumerate(ratio) if r == min_ratio]
    best_index = min(candidates, key=lambda i: price[i])
    print(f"{size[best_index]:.2f} {price[best_index]:.2f}")

main()
