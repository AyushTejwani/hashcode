# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 23:16:23 2021

@author: tejwa
"""

D=int(input())
I=int(input())
S=int(input())
V=int(input())
F=int(input())
start=[]
end=[]
street=[]
time=[]
for i in range(0,S):
    start.append(int(input()))
    end.append((input()))
    street.append(input())
    
    time.append(int(input()))

car_no_of_streets=[]
car_street=[]
for i in range(0,V):
    x=(int(input()))
    car_no_of_streets.append(x)
    asd=[]
    for j in range(0,x):
        asd.append(input())
    car_street.append(asd)
        
print(D)
print(I)    
print(S)
print(V)
print(F)
for i in range(0,S):
    print(start[i])
    print(end[i])
    print(street[i])
    print(time[i])
 