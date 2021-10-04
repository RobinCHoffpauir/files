import pybaseball
import pandas as pd
from pandas import options
pd.options.display.max_columns = None
pd.options.display.max_rows = None
import csv 
from pybaseball import schedule_and_record
df=pd.DataFrame(schedule_and_record(start_season='2021','COL'))
input('press <enter>')
