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
streets=[]
for i in range(0,S):
    start=(int(input()))
    end=(int(input()))
    street=(input())
    time=(int(input()))
    onestreet={
        "start":start,
        "end":end,
        "street":street,
        "time":time
        }
    streets.append(onestreet)
   
for i in range(0,S):
    print(streets[i])
car_no_of_streets=[]
car_street=[]
cars=[]
for i in range(0,V):
    x=(int(input()))
   
    
    asd=[]
    for j in range(0,x):
        asd.append(input())
    one_car={
        'streets_visited':x,
        'names_of_streets':asd}
    car_street.append(one_car)

for i in range(0,V):
    print(car_street[i])
        

 