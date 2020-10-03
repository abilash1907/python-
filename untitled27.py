# -*- coding: utf-8 -*-
"""
Write a python program to create a dictionary of phone numbers and names of five
persons. Display the contents of the dictionary in alphabetical order of names
"""
n = {}
for i in range(2):
    x = input("enter name")
    y = int(input("enter number"))
    n[x]= y
print(n)
k = list(n)
k.sorted()
k = dict[n]
print(k)

    