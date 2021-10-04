# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 01:51:24 2021

@author: Robin
"""
import mlbgame as mlb
import pandas as pd
games = mlb.games(2021,9,16)
x=games[0]
df = pd.DataFrame(columns=['Team','Runs','Hits','Errors'])
g0 = {'Team': x.away_team,'Runs' : x.away_team_runs,'Hits' : x.away_team_hits,'Errors' : x.away_team_errors}
g1 = {'Team': x.home_team,'Runs' : x.home_team_runs,'Hits' : x.home_team_hits,'Errors' : x.home_team_errors}
g1=pd.DataFrame(g1, index=[0])
g0 = pd.DataFrame(g0, index = [0])
df = df.append([g0,g1])