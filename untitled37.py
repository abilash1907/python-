# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 23:00:05 2019

@author: admin
"""

a = {'0':"zero",'1':"one",'2':"two",'3':"three",'4':"four",'5':"five",'6':"six",'7':"seven",'8':"eight",'9':"nine",'10':"ten"}
f = input("enter number")
c = []
for i in range(0,len(f)):
    c.append(f[i])
for j in c:    
    if j in a.keys():
        f = a[j]
        print(f,end = " ")
        
    