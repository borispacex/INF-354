# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:43:21 2019

@author: INF-322
"""

from kanren import run, eq, membero, var, conde
x = var()
z = var()
print(run(1, x, eq(x, 5)))
print(run(1, x, eq(x, z), eq(z, 3)))
print(run(1, x, eq((1, 2), (1, x))))

from kanren import Relation, facts
parent = Relation()
facts(parent, ("Homer", "Bart"),("Homer", "Lisa"),("Abe",  "Homer"))
print(run(1, x, parent(x, "Bart")))
print(run(1, x, parent("Homer", x)))
print(run(3, x, parent("Homer", x)))

y = var()
print(run(1, x, parent(x, y), parent(y, 'Bart')))

def grandparent(x, z):
    y = var()
    return conde((parent(x, y), parent(y, z)))

print(run(1, x, grandparent(x, 'Bart')))
print(run(2, x, membero(x, (1, 2, 3)), membero(x, (2, 3, 4))))



x, y = var(), var()
print( run(0, x, eq(y, (1, 2, 3)), (membero,x, y))  )


x = [1,2,3,4,5]
print(x)


