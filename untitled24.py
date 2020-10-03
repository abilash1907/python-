# -*- coding: utf-8 -*-
"""
Write a python program that opens a file for input and prints 
the count of four letter words
in it. 
"""
n = input("enter the string ")
f = open("new.txt","w")
f.write(n)
f.close()
f = open("new.txt","r")
c = f.read()
count = 0
for i in c.split():
    if len(i)== 4:
        count+= 1
print(count)