# -*- coding: utf-8 -*-
"""
Created on Mon May 20 10:58:31 2019

@author: INF-322
"""

from sklearn import datasets
from sklearn.cluster import KMeans

iris = datasets.load_iris()
X=iris.data
y=iris.target

grupos = KMeans(n_clusters=3)
grupos.fit(X)
print("predecido")
print(grupos.labels_)
print("original")
print(y)

from sklearn.metrics import confusion_matrix as cm
print(cm(y, grupos.labels_))