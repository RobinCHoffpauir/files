import pybaseball
import pandas as pd
from pandas import options
pd.options.display.max_columns = None
pd.options.display.max_rows = None
import csv
import matplotlib
from matplotlib import pyplot as plt
from pybaseball import team_game_logs
battinglog=pd.DataFrame(team_game_logs(2019, "COL"))
pitchinglof=pd.DataFrame(team_game_logs(2019,"COL",'pitching'))
logs=pd.concat([battinglog,pitchinglog],index=1)
print(logs)
input("press <enter>")
