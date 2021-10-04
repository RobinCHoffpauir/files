# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 03:14:10 2021
API calls for Rental and Sales listings and approximates of sale values
@author: Robin
"""
#NAVAREE RENTAL LISTING
import requests
from pandas import read_json as rj
import pandas as pd
pd.options.display.max_columns=None
pd.options.display.max_rows=None
def rentals(city,state):
    """
    rental properties available in specified city(full name), state(2 letter abbr.)

    Parameters
    ----------
    city : ex.'Denver',type(str)
    state : ex.'CO', type(str)

    Returns
    -------
    1.a requests module http response
    2.a GET call via requests module(W/querystring&headers)
    3.a .text call to the JSON file that is returned from requests

    """
    global rent_df
    url = "https://realty-mole-property-api.p.rapidapi.com/rentalListings"
    querystring = {"city":city,"state":state}

    headers = {
    'x-rapidapi-host': "realty-mole-property-api.p.rapidapi.com",
    'x-rapidapi-key': "b501e0bf75mshf881260fcf61406p1a7f13jsnbce859978dd1"
     }
    ##^^^just our rapidapikeys and whatnot
    response = requests.request("GET", url, headers=headers, params=querystring)
    #using our var for read_json
    rent_df = rj(response.text)
    print(rent_df)


def listings(city,state):
    global list_df
    url = "https://realty-mole-property-api.p.rapidapi.com/saleListings"

    querystring = {"city":"Austin","state":"TX"}

    headers = {
        'x-rapidapi-host': "realty-mole-property-api.p.rapidapi.com",
        'x-rapidapi-key': "b501e0bf75mshf881260fcf61406p1a7f13jsnbce859978dd1"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    list_df = rj(response.text)
    print(list_df)