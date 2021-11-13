# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 17:53:57 2021

@author: robin
"""

# %% imports
import requests
import pandas as pd

# %% scrape tables with pandas
url = 'https://www.covers.com/sport/football/nfl/printsheet'

# Create a pandas DF 'table' to hold table data
table = pd.read_html(url)
table = table[2]

# set the 4th row as the column names
table.columns = table.iloc[3]

# now we will slice and append data to clean up table
nfl = pd.DataFrame()
nfl = nfl.append(table[4:6])
nfl = nfl.append(table[9:31])
nfl = nfl.append(table[34:36])


# clean the data further
nfl.index = nfl['Gm#']
nfl = nfl.drop('Gm#', axis=1)
nfl.columns = ['Team', 'Ovr SU W/L', 'Ovr ATS', 'Ovr AF-AA', 'OffRu', 'OffPa', 'OffTot', 'DefRu', 'DefPa', 'DefTot',
               'TO',
               'ToP', 'H/A SU W/L', 'H/A ATS', 'H/A AF-AA', 'Streak SU', 'Streak ATS', 'Streak O/U']
