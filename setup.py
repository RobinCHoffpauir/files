1
# import packages and pybaseball modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import pickle
import warnings
from pybaseball import schedule_and_record
from pybaseball import statcast
from pybaseball import playerid_lookup
from pybaseball import statcast_pitcher
from pybaseball import team_batting
from pybaseball import team_pitching
from pybaseball import batting_stats_range
from pybaseball import pitching_stats_range
from pybaseball import statcast_single_game
from pybaseball import playerid_reverse_lookup

class player(fname,lname):
    """