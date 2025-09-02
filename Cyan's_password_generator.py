# -*- coding: utf-8 -*-
"""
Module: Cyan's_password_generator
Author: zen
Date: 5/8/2025 AD
"""

def main():
    '''Main Function'''
    firstname = str(input())
    lastname = str(input())
    age = int(input())
    passwd = ""

    if len(firstname) >= 5 and len(lastname) >= 5:
        passwd += firstname[0:2] + lastname[-1] + str(age)[-1]
    else:
        passwd += firstname[0:1] + str(age) + lastname[-1]
    print(passwd)

main()
