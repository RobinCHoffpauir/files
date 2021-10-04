# -*- coding: utf-8 -*-
"""
Spyder Editor

yahoo finance
"""
from sklearn import tree
X = mlb[['wRC+','WAR','wOBA','Off']]
Y = mlb['wins']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
predict=clf.predict(Y)
print(predict)
