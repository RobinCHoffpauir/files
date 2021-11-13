# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 05:00:55 2021

@author: robin
"""
import bs4
import pandas as pd
import requests


def get_matchup(team1, team2):
    """
    retrieve table from ESPN's hollinger stats including Pace, Off Eff, etc

    Parameters
    ----------
    team : TYPE str 'SACRAMENTO'
        DESCRIPTION. FULL TEAM NAME, Capital first letter

    Returns
    -------
    table of float64 numbers, of two specified teams (team1, team2 variables) 
    under the variable = matchup

    """
    r = requests.get('http://www.espn.com/nba/hollinger/teamstats/_/sort/paceFactor').text
    global table
    table = pd.read_html(r)
    table = table[0]
    table.columns = table.iloc[1]
    del table['RK']
    table = table.drop([0,1])
    table.index = table['TEAM']
    table = table.drop(['TEAM', 'DRR'], axis = 1)
    table = pd.DataFrame(table)
    table[['PACE', 'AST', 'TO', 'ORR', 'REBR', 'EFF FG%', 'TS%', 'OFF EFF',
       'DEF EFF']] = table[['PACE', 'AST', 'TO', 'ORR', 'REBR', 'EFF FG%', 'TS%', 'OFF EFF',
       'DEF EFF']].astype(float)
    global matchup
    matchup = table.loc[[team1, team2]]
    return matchup