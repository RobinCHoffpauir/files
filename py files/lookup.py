import pybaseball
import pandas as pd
from pandas import options
pd.options.display.max_columns = None
pd.options.display.max_rows = None
import csv
from pybaseball import playerid_lookup
player=csv.read_csv('/Users/Robin/Documents/batting_stats_2021.csv')
input('press <enter>')
for val in player.itterrows():
    print(val)
input('press <enter<')
