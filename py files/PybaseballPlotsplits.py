# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pybaseball as pyb
import pandas as pd
import matplotlib.pyplot as plt

from pybaseball import statcast, statcast_batter, spraychart, playerid_lookup, player_search_list
from pybaseball.plotting import plot_bb_profile

player_1 = 'Ohtani'
player1 = playerid_lookup(player_1)
key = int(player1['key_mlbam'])

data = statcast_batter('2019-04-01','2021-09-14', key)

v_lhp_splits = data[data['p_throws']== 'L']
v_rhp_splits = data[data['p_throws']== 'R']

lhp_sp = v_lhp_splits[v_lhp_splits['home_team']=='LAA']
rhp_sp = v_rhp_splits[v_rhp_splits['home_team']=='LAA']

comb_splits = pd.concat([v_lhp_splits, v_rhp_splits])

spraychart(comb_splits, 'angels', title='Shohei Ohtanis hit locations in Angels stadium')
plot_bb_profile(comb_splits,parameter=('launch_angle'))