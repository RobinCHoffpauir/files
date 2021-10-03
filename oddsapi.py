import pandas as pd
import oddsapi as odds
pd.options.display.max_rows = None
pd.options.display.max_columns = None
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 21:08:55 2021

@author: Robin
"""
"""
Odds API to pull realtimed sportsbook odds
"""

key = ('0da58289481531bb44567ffcf3484b51')
baseball = 'baseball_mlb'
client = odds.OddsClient(api_key=key)
sports = client.retrieve_sports()
odds = client.retrieve_odds(sport_key=baseball, region='us', mkt='h2h')
Odds = pd.DataFrame(odds)

sites=(Odds['sites'])
pd.DataFrame(sites,columns=['site key', 'site','last update', 'odds'])