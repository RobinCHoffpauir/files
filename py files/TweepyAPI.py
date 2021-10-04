# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 00:18:42 2021
Twitter API info and stuff
@author: Robin
"""
import tweepy
import twitter
access_token = '1356107487619891200-JpLxNYg9IHDdcbZvJ645UuPYbz50Nx'
token_secret = 'KjeaNC0LSduA1tgX4sdBGOaewmO3pdvG5uFNE2Tqu3rEb'
api_key = "ZYyNpytFi1N8h7cDKBz0ZPwyY"
key_secret = "8Y2PzqtjyHaUeVv8J6nC1pUUJbvepp9vjuS01cek7KDlQIbEix"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAHU2TgEAAAAA%2BEVzX9XXJnFU0y1HrUwaNNW2eNs%3DQBIJybJcb9bHLQjQggvgbnKuWxYhfz03TygM8aQr28aO5UZSVR"

auth = tweepy.OAuthHandler(api_key, key_secret)
api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.search, q="tweepy").items(10):
    print(tweet.text)

