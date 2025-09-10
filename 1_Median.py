# -*- coding: utf-8 -*-
"""
Module: 1_Median
Author: zen
Date: 10/9/2025 AD
"""
import json
def main():
    """Main Function"""
    raw_text = input().strip()
    text = f"[{raw_text}]"
    myList = json.loads(text)
    myList.sort()

    n = len(myList)
    if not n % 2:
        median = (myList[n // 2 - 1] + myList[n // 2]) / 2
    else:
        median = myList[n // 2]

    print(f"{median:.2f}")

main()
