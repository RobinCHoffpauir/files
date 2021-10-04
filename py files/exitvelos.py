import pybaseball
import pandas as pd
from pandas import options
pd.options.display.max_columns = None
pd.options.display.max_rows = None
import csv 
from pybaseball import playerid_lookup
from pybaseball import statcast_batter_exitvelo_barrels

z=statcast_batter_exitvelo_barrels(2021)
data=pd.DataFrame(z)
data.to_clipboard(sep=',')
print(data)
input('press <enter>')



