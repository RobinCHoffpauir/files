# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 15:38:26 2021

@author: robin
"""
# %% imports
import requests
import pandas as pd

# %% scripts
class NBA:
    def __init__(self):
        NBA.team = team
        NBA.team2 = team2
        NBA.player = player

    def get_player_stats(player):
        """
        retrieve player stats from yahoo.com nba stats

        Returns
        -------
        table with individual player stats

        """
        global players
        p = pd.read_html(
            "https://sports.yahoo.com/nba/stats/individual/?selectedTable=0"
        )
        players = p[0]
        del p
        return players

    def get_team_stats(team, team2=None):
        """
        returns DataFrame of team_stats from yahoo.com nba stats

        Returns
        -------
        table with team stats

        """
        global teams
        t = pd.read_html("https://sports.yahoo.com/nba/stats/team/")
        teams = t[0]
        del t
        if team in teams["Team"]:
            print(teams.loc[team])
        else:
            pass
        if team2 == None:
            pass
        else:
            print(teams.loc[team2])
        return teams

    def get_matchup(team, team2):
        """
        retrieve table from ESPN's hollinger stats including Pace, Off Eff, etc
        Parameters
        ----------
        team : TYPE str 'SACRAMENTO'
        DESCRIPTION. FULL TEAM NAME, Capital first letter
        Returns
        -------
        table of float64 numbers, of two specified teams (team1, team2
                                                          variables)
        under the variable = matchup
        """
        r = requests.get(
            "http://www.espn.com/nba/hollinger/teamstats/_/sort/paceFactor"
        ).text
        global table
        table = pd.read_html(r)
        table = table[0]
        table.columns = table.iloc[1]
        del table["RK"]
        table = table.drop([0, 1])
        table.index = table["TEAM"]
        table = table.drop(["TEAM", "DRR"], axis=1)
        table = pd.DataFrame(table)
        table[
            ["PACE", "AST", "TO", "ORR", "REBR", "EFF FG%", "TS%", "OFF EFF", "DEF EFF"]
        ] = table[
            ["PACE", "AST", "TO", "ORR", "REBR", "EFF FG%", "TS%", "OFF EFF", "DEF EFF"]
        ].astype(
            float
        )
        global matchup
        matchup = table.loc[[team, team2]]
        return matchup
