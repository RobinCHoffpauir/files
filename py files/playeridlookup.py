import pybaseball
import pandas as pd
from pandas import options
pd.options.display.max_columns = None
pd.options.display.max_rows = None
import csv
import matplotlib
from matplotlib import pyplot as plt
from pybaseball import playerid_lookup
player=[]
x=input('what player are you searching for? firstname')
y=input('what last name')
player=playerid_lookup(str(y),str(x))
input('press <enter>')
playerid=player['key_mlbam']
print(playerid)          
input('press <enter>')

    

      
