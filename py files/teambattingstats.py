import pybaseball
import pandas as pd
from pandas import options
pd.options.display.max_columns = None
pd.options.display.max_rows = None
import csv
from pybaseball import team_batting
X=pd.DataFrame(team_batting(2020))
print(X)
input('press <enter>')
