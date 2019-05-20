# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:36:28 2019

@author: INF-322
"""

x = [1, 1, 1, 1, 1, 1, 1, 1]
y = [256,128,64,32,16,8,4,2,1]
posicion=len(x)-1
suma = 0
for i in range(len(x)):
    suma = suma + (x[posicion]*y[posicion])
    posicion=posicion-1
print(suma)    
print(suma**2)
print(sum(y))



