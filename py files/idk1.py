# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 00:52:54 2021

@author: Robin
"""

data = mlbgame.game.scoreboard(2021, 9, 14, home=None, away=None)
print([mlbgame.game.GameScoreboard(data[x]) for x in data])