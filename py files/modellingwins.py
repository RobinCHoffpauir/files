import pybaseball
import pandas as pd
from pandas import options
pd.options.display.max_columns = None
pd.options.display.max_rows = None
import csv
import matplotlib
from matplotlib import pyplot as plt
from pybaseball import lahman
teams=lahman.teams()
teams_df=pd.DataFrame(teams)
drop_cols = ['lgID','franchID','divID','Rank','Ghome','L','DivWin','WCWin','LgWin','WSWin','SF','name','park','attendance','BPF','PPF','teamIDBR','teamIDlahman45','teamIDretro','franchID','franchName','active','NAassoc']
df=teams_df.drop(drop_cols, axis=1)
print(teams_df)
print(df['W'].mean())
def assign_win_bins(W):
    if W < 50:
        return 1
    if W >= 50 and W <= 69:
        return 2
    if W >= 70 and W <= 89:
        return 3
    if W >= 90 and W <= 109:
        return 4
    if W >= 110:
        return 5
df['wins_bins']=df['W'].apply(assign_win_bins)    
input('press <enter>')
