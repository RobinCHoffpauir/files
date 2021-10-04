# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 17:50:20 2021

@author: Robin
"""

import numpy as np
import pandas as pd
import pybaseball as pyb
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import warnings
warnings.filterwarnings('ignore')

pitches = data
#print('Our dataset has {0} Pitches'.format(len(pitches)))

#plot pitch_types
sns.catplot(x='release_speed', y='release_spin_rate', hue='pitch_name', data=pitches[:500])

def decision_tree(data, fastball_group):
    data = data.loc[:,['pitch_name', 'release_speed', 'release_spin_rate', 'vx0', 'vy0', 'vz0', 'ax', 'ay', 'az']]
    
    data = data.dropna()
    
    def pitch_filter(x):
        if x=='2-Seam Fastball' or x=='4-Seam Fastball' or x=='Sinker':
            return 'Fastball_group'
        return x
    if fastball_group == True:
        data['pitch_name'] = data['pitch_name'].apply(pitch_filter)
        
    X = data.loc[:,['release_speed', 'release_spin_rate', 'vx0', 'vy0', 'vz0', 'ax', 'ay', 'az']]
    y = data.loc[:,['pitch_name']]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=8)
    
    dt_model = tree.DecisionTreeClassifier(max_depth=10, min_samples_split=50)
    
    dt_model.fit(X_train, y_train)
    
    predictions = dt_model.predict(X_test)
    print('Test Score Accuracy {0}'.format(accuracy_score(predictions, y_train)))
    
    predictions = dt_model.predict(X_test)
    print('Test Score Accuracy {0}'.format(accuracy_score(predictions, y_test)))
    
    print(classification_report(predictions, y_test))
    
decision_tree(pitches, fastball_group = False)