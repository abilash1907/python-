# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 20:42:02 2018

@author: admin
"""

a = []
for i in range(int(input("enter range"))):
    b = []
    for j in range(2):
        name = input()
        score = float(input())
        b.append(name)
        b.append(score)
    a.append(b)
print(a)