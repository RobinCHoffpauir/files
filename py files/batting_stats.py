import pybaseball
import numpy
import pandas as pd
from pandas import options
pd.options.display.max_columns = None
pd.options.display.max_rows = None
from pybaseball import batting_stats
x=input('Enter Year:  ')
df=pd.DataFrame(batting_stats(x))
input("Press <enter>")
print(df)
df.to_csv('/Users/Robin/My Documents/batting_stats_')
input("Press <enter>")
