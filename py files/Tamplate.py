# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 17:19:21 2021

@author: Robin
"""

import pybaseball as pyb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as skl
import seaborn as sns
pd.options.display.max_rows=None
pd.options.display.max_columns=None
x=pyb.batting_stats_bref(2021)
z=pyb.teams()
z = z[z['yearID']>1995]
sns.lmplot(x='HR', y='W',data=z, hue='ERA',legend=False)
