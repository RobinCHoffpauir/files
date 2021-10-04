import pybaseball
import pandas as pd
from pandas import options
pd.options.display.max_columns = None
pd.options.display.max_rows = None
import csv
import matplotlib
from matplotlib import pyplot as plt
from pybaseball import statcast_batter, spraychart
votto_data = statcast_batter('2019-08-01', '2019-10-01', 458015)
aquino_data = statcast_batter('2019-08-01', '2019-10-01', 606157)
data = pd.concat([votto_data, aquino_data])
home_data = data[data['home_team'] == 'CIN']
spraychart(home_data, 'reds', title='Joey Votto vs. Aristedes Aquino', colorby='player')
