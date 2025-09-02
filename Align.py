# -*- coding: utf-8 -*-
"""
Module: Align
Author: zen
Date: 30/8/2025 AD
"""


def main():
    '''Main Function'''
    target_lens = int(input())
    alignment = str(input())
    raw_text = str(input())
    free_space = int(len(raw_text) - target_lens)

    if alignment == 'left':
        print(raw_text+""*free_space)
    elif alignment == 'right':
        print(" "*free_space+raw_text)
    elif alignment == 'center':
        print(" " * int(free_space/2) + raw_text + " "*int(free_space/2))

main()
