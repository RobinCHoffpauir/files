c  # -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 23:03:49 2021
saving a PYB dataframe to csv
@author: Robin
"""

df = pyb.teams()
df = df[df['yearID'] >= 2015]
df = df['franchID']
df = df.drop_duplicates(keep='first')
df[2789] = 'MIA'
df[2787] = 'LAA'
df[2801] = 'TBR'
for t in df:
    for num in range(2010, 2021):
        team_p = pyb.team_pitching(start_season=num, team=t)\

dataframe = pd.DataFrame()
for t in df:
    x = pyb.schedule_and_record(2021, t)
    dataframe = dataframe.append(x, ignore_index=True)

dataframe = dataframe.drop('Orig. Scheduled', axis=1)
dataframe = dataframe.dropna()
dataframe.to_csv('C:/Users/Robin/team_sched&rec.csv', sep=',')
