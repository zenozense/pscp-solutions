# -*- coding: utf-8 -*-
"""
Module: BrickBridge
Author: zen
Date: 4/9/2025 AD
"""
def main():
    """Main Function"""
    small_brick = int(input())
    large_brick = int(input())
    target = int(input())

    max_large_needed = target // 5
    large_used = min(large_brick, max_large_needed)

    remaining = target - (large_used * 5)

    if remaining <= small_brick:
        print(remaining)
    else:
        print("-1")

main()
