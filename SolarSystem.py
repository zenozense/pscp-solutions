# -*- coding: utf-8 -*-
"""
Module: SolarSystem
Author: zen
Date: 15/7/2025 AD
"""


def main():
    '''Main Function'''
    FullString = str(input())
    counter = 0
    Sun_pos = 0
    Hottest = ""
    Coldest = ""

    planets = FullString.split()
    for planet in planets:
        counter += 1
        if planet == "Sun":
            Sun_pos = counter
        else:
            pass

    if planets[8] == "Sun":
        Hottest = planets[7]
        Coldest = planets[0]
    elif planets[0] == "Sun":
        Hottest = planets[Sun_pos]
        Coldest = planets[-1]
    else:
        Hottest = planets[Sun_pos-2] + f" {planets[Sun_pos]}"
        Coldest = planets[8-Sun_pos]

    print(f"Hot: {Hottest}\nCool: {Coldest}")

main()
