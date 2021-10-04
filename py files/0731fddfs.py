# -*- coding: utf-8 -*-



import pydfs_lineup_optimizer as dfs
from pydfs_lineup_optimizer import get_optimizer,Site,Sport
optimizer=get_optimizer(Site.FANDUEL, Sport.BASEBALL)
optimizer.load_players_from_csv("FanDuel-MLB-2021-07-31-62229-entries-upload-template.csv")
optimizer.restrict_positions_for_opposing_team(['P'], ['C','SS','OF','1B','2B','3B'])
for lineup in optimizer.optimize(n=10,max_exposure=0.3):
    print(lineup)
    print(lineup.players)
optimizer.export('results.csv')