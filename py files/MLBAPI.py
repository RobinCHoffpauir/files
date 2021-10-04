# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 21:02:03 2021

@author: Robin
"""

import requests
import pandas as pd


class teams:

    ##TEAMS List
    def active_teams():
        r = requests.get(
            "https://api.sportsdata.io/v3/mlb/scores/json/teams?key=54950d5588954b3da5d00e54e3ac5d1b"
        )
        json = r.json()
        data = pd.DataFrame(json)

    ##players by team
    def players_by_team():
        r = requests.get(
            "https://api.sportsdata.io/v3/mlb/scores/json/Players/%7Bteam%7D?key=54950d5588954b3da5d00e54e3ac5d1b"
        )
        json = r.json()
        data = pd.DataFrame(json)

        r = requests.get(
            "https://api.sportsdata.io/v3/mlb/odds/json/BettingMetadata?key=54950d5588954b3da5d00e54e3ac5d1b"
        )
        json = r.json()
        data = pd.DataFrame(json)

        r = requests.get(
            "https://api.sportsdata.io/v3/mlb/scores/json/Players/%7Bteam%7D?key=54950d5588954b3da5d00e54e3ac5d1b"
        )
        json = r.json()
        data = pd.DataFrame(json)

        r = requests.get(
            "https://api.sportsdata.io/v3/mlb/scores/json/Players/%7Bteam%7D?key=54950d5588954b3da5d00e54e3ac5d1b"
        )
        json = r.json()
        data = pd.DataFrame(json)

        r = requests.get(
            "https://api.sportsdata.io/v3/mlb/scores/json/Players/%7Bteam%7D?key=54950d5588954b3da5d00e54e3ac5d1b"
        )
        json = r.json()
        data = pd.DataFrame(json)
