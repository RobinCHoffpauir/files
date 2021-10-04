import pybaseball
import pandas as pd
from pandas import options
pd.options.display.max_columns = None
pd.options.display.max_rows = None
import csv 
from pybaseball import batting_stats_bref
df=pd.DataFrame(batting_stats_bref(2021))
df.to_csv('/Users/Robin/PYTHON3.9/batting_stats_bref.csv' sep=',')
print(df)
input('press <enter>')

