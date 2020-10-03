# -*- coding: utf-8 -*-
"""
Write a python code to tind transpose of a matrix using list

"""
n = int(input("enter no of rows"))
x = int(input("enter no of coloums"))
a = []
b = []
for i in range(x):
    c = []   
    for j in range(n):
        e = int(input("enter the number"))
        c.append(e)        
    a.append(c)
for j in range(n):
    d = []   
    for k in range(x):        
        d.append(0)        
    b.append(d)  
for l in range(len(a)):
    for m in range(len(a[l])):
        b[m][l]= a[l][m]
print("transpose of",a,"is")
for n in b:
    print(n)