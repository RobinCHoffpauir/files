# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 11:17:48 2021

@author: Robin
"""
import pandas as pd
import sklearn as skl
from sklearn import datasets, neighbors
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
iris = datasets.load_iris()
x = iris.data
y = iris.target
knn=skl.neighbors.KNeighborsClassifier(n_neighbors=6)
knn.fit(iris['data'], iris['target'])
x_new= np.array([[5.6, 2.8, 3.9, 1.1],[5.7, 2.6, 3.8, 1.3],[4.7, 3.2, 1.3, 0.2]])
prediction=knn.predict(x_new)
print('Prediction: {}'.format(prediction))