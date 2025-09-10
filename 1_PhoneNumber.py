# -*- coding: utf-8 -*-
"""
Module: 1_PhoneNumber
Author: zen
Date: 10/9/2025 AD
"""

def main():
    """Main Function"""
    phone = input().strip()
    which_type = input().strip()
    store = ""
    timeq = 0

    if which_type == "International":
        if phone.startswith("0"):
            phone = phone[1:]

    for value in reversed(phone):
        store += value
        timeq += 1
        if timeq == 4:
            store += " "
            timeq = 0

    formatted = store[::-1].strip()

    if which_type == "Domestic":
        print(formatted)
    else:
        print("+66" + formatted)

main()
