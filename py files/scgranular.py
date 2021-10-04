import pandas as pd
import pybaseball as pyb
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as skl
from sklearn import *
# enable the cache for quicker reqall of statcast data
# or another option is to comment out the serach after completed
pyb.cache.enable()
# get the statcast data with our params set
# to be the passed variables in our function
# then lets drop the deprecated empty
# columns with .dropna(axis=1, how 'All')

# create a global instance
global ef
global df


def sc_events(st_date, end_date):
    """
    to find all events  that are put
    in play via statcast

    Parameters
    ----------
    st_date :'YYYY-MM-DD' ISOformat dt.
    end_date : 'YYYY-MM-DD' ISOformat dt.

    Returns
    -------
    dataframe containing pitch by pitch
    data of statcast that has been filtered
    to only include pitches that were put in play

    """
    df = pyb.statcast(st_date, end_date)
    df = df.dropna(axis=1, how='all')
    global df = df[df['type'] == 'X']


# get the statcast data with our params set
# to be the passed variables in our function
# lets drop the deprecated empty columns with .dropna(axis=1, how 'All')
# now drop all pitches that are put in play

def sc_na_events(st_date, end_date):
    """
    to find all events  that are NOT put
    in play via statcast

    Parameters
    ----------
    st_date :'YYYY-MM-DD' ISOformat dt.
    end_date : 'YYYY-MM-DD' ISOformat dt.

    Returns
    -------
    dataframe containing pitch by pitch
    data of statcast that has been filtered
    to only include pitches that were NOT put in play

    """
    ef = pyb.statcast(st_date, end_date)
    ef = ef.dropna(axis=1, how='all')
    global ef = ef[ef['type'] != 'X']
