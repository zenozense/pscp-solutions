# -*- coding: utf-8 -*-
"""
Module: Colors
Author: zen
Date: 19/7/2025 AD
"""


def main():
    '''Main Function'''
    first_color = str(input())
    second_color = str(input())

    if ((first_color == "Red" and second_color == "Yellow") or
            (first_color == "Yellow" and second_color == "Red")):
        print("Orange")
    elif ((first_color == "Red" and second_color == "Blue") or
          (first_color == "Blue" and second_color == "Red")):
        print("Violet")
    elif ((first_color == "Yellow" and second_color == "Blue") or
          (first_color == "Blue" and second_color == "Yellow")):
        print("Green")
    elif first_color == "Yellow" and second_color == "Yellow":
        print("Yellow")
    elif first_color == "Blue" and second_color == "Blue":
        print("Blue")
    elif first_color == "Red" and second_color == "Red":
        print("Red")
    else:
        print("Error")

main()
