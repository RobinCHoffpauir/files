# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 03:22:09 2021

@author: Robin
"""

import pandas as pd
import csv
import matplotlib.pyplot as plt
import math
import seaborn as sns
import pydfs_lineup_optimizer as dfs
import pydfs_lineup_optimizer as dfs
from pydfs_lineup_optimizer import get_optimizer,Site,Sport, TeamStack
optimizer=get_optimizer(Site.FANDUEL, Sport.BASEBALL)
optimizer.load_players_from_csv('C:/Users/Robin/FanDuel-MLB-2021 ET-08 ET-05 ET-62385-players-list.csv')
optimizer.add_stack(TeamStack(3,['HOU']))
optimizer.add_stack(TeamStack(2,['TOR']))
for lineup in optimizer.optimize(n=6):
    print(lineup)
    print(lineup.players)
    print(lineup.fantasy_points_projection)
    print(lineup.salary_costs)
