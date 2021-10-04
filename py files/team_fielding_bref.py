import pybaseball
import pandas as pd
from pandas import options
pd.options.display.max_columns = None
pd.options.display.max_rows = None
import csv 
from pybaseball import team_fielding_bref
x=input('what team would you like to lookup? (team abb., start_year, end_year): ')
data=pd.DataFrame(team_fielding_bref(x),2021)
data.to_clipboard(sep=",")
print(data)
input('press <enter>')
