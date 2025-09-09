# -*- coding: utf-8 -*-
"""
Module: 1_LastStand
Author: zen
Date: 10/9/2025 AD
"""

import json

def main():
    """Main Function"""
    myList = json.loads(str(input()))
    for i in myList:
        print(i%10)

main()
