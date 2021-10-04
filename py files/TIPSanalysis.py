# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 22:42:49 2021

@author: Robin
"""
import seaborn as sns
import pandas as pd
import numpy as np

# import the tips dataset from seaborn
tips = sns.load_dataset('tips')

# create a ['tip%'] column by dividing tip by total_bill
tips['tip%'] = (tips['tip'] / tips['total_bill'])

# get some descriptive stats about the tips df and we will
# plot the results of correlation (.corr()) to heatmap
corr = tips.corr()
desc = tips.describe()
isna = tips.isna().sum()
sns.heatmap(corr, annot=True, cmap='gnuplot')

# using the pairplot lets get a few visuals
sns.pairplot()

sns.relplot(x='total_bill', y='tip', hue='day', data=tips)
