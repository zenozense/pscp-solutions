# -*- coding: utf-8 -*-
"""
Module: Meteorite
Author: zen
Date: 5/8/2025 AD
"""

def fire(weight, parts, safe_weight):
    """DocString"""
    if weight < safe_weight:
        return 0
    total = 1
    new_weight = weight / parts
    i = 0
    while i < amount:
        total += fire(new_weight, parts, safe_weight)
        i += 1
    return total

first_kg = float(input())
amount = int(input())
require_kg = float(input())

missile = fire(first_kg, amount, require_kg)
print(missile)
