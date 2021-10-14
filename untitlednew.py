# -*- coding: utf-8 by Dongley99-*-
"""
2.Write a python program to compute the sum of first n positive
integers using recursion function
"""
def sUm(n):
    if n == 0:
        return 1
    else:
        return( n + sUm(n-1))
n = int(input("enter no"))
print(sUm(n))