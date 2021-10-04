# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 19:55:16 2021
EDA of the seaborn dataset "MPG", a dataset that contains car models and their attributes (mpg, weight, model_year, cylinders, etc..)
@author: Robin
"""
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import sklearn

pd.options.display.max_rows = None
pd.options.display.max_columns = None
# Load the dataset
mpg = sns.load_dataset("mpg")

# now for some exploritory analysis of the dataset
desc = mpg.describe()
info = mpg.info()
print(desc, info)


# plot some of our EDA
int_cols = mpg[["mpg", "displacement", "horsepower", "acceleration"]]
float_cols = mpg[["cylinders", "weight", "model_year"]]
obj_cols = mpg[["origin", "name"]]

sns.scatterplot(x="weight", y="mpg", data=mpg, hue="model_year", alpha=0.75)
sns.kdeplot(x="weight", y="mpg", data=mpg)
