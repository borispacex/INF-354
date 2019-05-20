# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:45:04 2019

@author: INF-322
"""

X=[[1,0,2], [1,1,3], [0,0,1], [0,1,0]] 
y=[0,1,0,1]

from sklearn.neural_network import MLPClassifier

clasificador = MLPClassifier(hidden_layer_sizes=(3,10,),solver='lbfgs')
clasificador.fit(X,y)
print(clasificador.predict([[1,0,1]]))

from sklearn import datasets
iris = datasets.load_iris()
X = iris.data
y = iris.target 
clasificador2= MLPClassifier(hidden_layer_sizes=(4,100,), activation="relu")
clasificador2.fit(X,y)
print(clasificador2.predict([[5.9,4.,5.1,0],[4.6,3.1,1.5,2]]))

import pandas as pd
data = pd.read_csv("ecoli.data")
#X = data[]
y = data['c9']
X = pd.DataFrame(data,columns=['c2','c3','c4','c5','c6','c7','c8'])
clasificador3= MLPClassifier( activation="relu")
clasificador3.fit(X,y)


y_pred = clasificador3.predict(X[10:20])
y_orig = y[10:20]

from sklearn.metrics import confusion_matrix as cm
print(cm(y_orig, y_pred))








