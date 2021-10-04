# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a Template for DFS Optimizer, MLB on Fanduel to be particular the first example is the basic usage
the seond will be the advanced usage"""
"""
BASIC
import pydfs_lineup_optimizer as dfs
from pydfs_lineup_optimizer import get_optimizer,Site,Sport
optimizer=get_optimizer(Site.FANDUEL, Sport.BASEBALL)
optimizer.load_players_from_csv(" *INSERRT PATH TO CSVFILE")
for lineup in optimizer.optimize(n=10):
    print(lineup)
    print(lineup.players)
    print(lineup.fantasy_points_projection)
    print(lineup.salary_costs)
"""
"""
ADVANCED
import pydfs_lineup_optimizer as dfs
from pydfs_lineup_optimizer import get_optimizer,Site,Sport
optimizer=get_optimizer(Site.FANDUEL, Sport.BASEBALL)
optimizer.load_players_from_csv(" *INSERRT PATH TO CSVFILE")
nets_centers=filter(lambda P: p.team =='Nets' and 'C'in p.positions, optimizer.players)
for player in nets_centers:
    optimizer.remove_player(*PLAYER*)   #this removes all nets players for optimizer
harden=optimizer.get_player_by_name('Harden')
irving=optimizer.get_player_by_name('Irving')     ##getirving and harden
harden.max_exposure(0.6)
irving.max_exposure(0.4)
optimizer.add_player_to_lineup(harden)
optimizer.add_player_to_lineup(irving)       ##locks in irving and harden
for lineup in optimizer.optimize(n=10,nax_exposure=0.3):
    print(lineup)
 optimizer.export('results.csv')
    
 
    ADDITIONS
--optimizer.set_players_from_one_team({'BOS':3})

--for player in optimizer.players:
    projected_ownership = get_projected_ownership(player)
optimizer.set_projected_ownership(max_projected_ownership = 0.5)

--optimizer.restrict_positions_for_opposing_team(['P'], ['C','SS','OF','1B','2B','3B'])