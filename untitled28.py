# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 20:52:47 2019

@author: admin
"""

n = int(input("enter no of rows"))
x = int(input("enter no of coloums"))
a = []
b = []
new = []
for i in range(x):
    c = []
    s = []
    for j in range(n):
        e = int(input("enter the number to 1st matrix"))
        l = int(input("enter the number to 2nd matrix"))
        s.append(l)
        c.append(e)        
    a.append(c)
    new.append(s)
for j in range(n):
    d = []   
    for k in range(x):        
        d.append(0)        
    b.append(d)  
for l in range(len(a)):
    for m in range(len(a[l])):
        b[l][m]= a[l][m] + new[l][m]
print("sum of two matrix is")
for n in b:
    print(n)