# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 01:58:44 2021

@author: Robin
"""

    
import pydfs_lineup_optimizer as dfs
from pydfs_lineup_optimizer import get_optimizer,Site, Sport, TeamStack
optimizer=get_optimizer(Site.FANDUEL, Sport.BASEBALL)
optimizer.load_players_from_csv('FanDuel-MLB-2021-08-01-62235-entries-upload-template (1).csv')
optimizer.add_stack(TeamStack(3, for_teams=[['SEA','CWS'], max_exposure=(0.75)))
optimizer.set_projected_ownership(max_projected_ownership = 0.75)
optimizer.restrict_positions_for_opposing_team(['P'], ['C','SS','OF','1B','2B','3B'])
for lineup in optimizer.optimize(n=20):
    print(lineup)
    print(lineup.players)
    print(lineup.fantasy_points_projection)
    print(lineup.salary_costs)
optimizer.export('0801fdlineups.CSV')
