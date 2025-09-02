# -*- coding: utf-8 -*-
"""
Module: BigFrame
Author: zen
Date: 11/8/2025 AD
"""

def main():
    '''Main Function'''
    a = str(input().strip(" "))
    b = str(input().strip(" "))
    c = str(input().strip(" "))
    d = str(input().strip(" "))
    e = str(input().strip(" "))

    my_dict = {1: a, 2: b, 3: c, 4: d, 5: e}

    length = max(len(a), len(b), len(c), len(d), len(e))
    full_length = int(length) + 4
    print(full_length*"*")
    for i in range(1, 6):
        last_space = full_length - (len(my_dict[i]) + 3)
        print("*", str(my_dict[i]) + " "*last_space+"*")

    print(full_length*"*")

main()
