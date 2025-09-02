# -*- coding: utf-8 -*-
"""
Module: ProgressiveTax
Author: zen
Date: 14/7/2025 AD
"""

def main():
    '''Main Function'''
    net_salary = int(input())
    tax = 0

    if net_salary > 4000000:
        tax += (net_salary - 4000000) * 0.35
        net_salary = 4000000
    if net_salary > 2000000:
        tax += (net_salary - 2000000) * 0.30
        net_salary = 2000000
    if net_salary > 1000000:
        tax += (net_salary - 1000000) * 0.25
        net_salary = 1000000
    if net_salary > 750000:
        tax += (net_salary - 750000) * 0.20
        net_salary = 750000
    if net_salary > 500000:
        tax += (net_salary - 500000) * 0.15
        net_salary = 500000
    if net_salary > 300000:
        tax += (net_salary - 300000) * 0.10
        net_salary = 300000
    if net_salary > 150000:
        tax += (net_salary - 150000) * 0.05
        net_salary = 150000

    print(int(tax))

main()
