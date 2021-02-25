# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 23:16:23 2021

@author: tejwa
"""
f=open("a.txt","r")
content=f.read()
cont=content.split()



D=int(cont[0])
I=int(cont[1])
S=int(cont[2])
V=int(cont[3])
F=int(cont[4])
streets=[]
for i in range(0,S):
    start=cont[4+i*4+1]
    end=cont[4+i*4+2]
    street=cont[4+i*4+3]
    time=cont[4+i*4+4]
    onestreet={
        "start":int(start),
        "end":int(end),
        "street":street,
        "time":int(time)
        }
    streets.append(onestreet)
   
for i in range(0,S):
    print(streets[i])
car_no_of_streets=[]
car_street=[]
cars=[]
x=0
for i in range(0,V):
   # print(4+S*4+i*(x+1)+1)
  #  print(cont[4+S*4+i*(x+1)+1])
    counter=4+S*4+i*(x+1)+1
    x=int(cont[4+S*4+i*(x+1)+1])
    asd=[]
    for j in range(0,x):
       # print(cont[4+S*4+i*(x+1)+2+j])
       # print(4+S*4+i*(x+1)+2+j)
        asd.append(cont[counter+1+j])
    one_car={
        'streets_visited':x,
        'names_of_streets':asd}
    car_street.append(one_car)

for i in range(0,V):
    print(car_street[i])
        

 