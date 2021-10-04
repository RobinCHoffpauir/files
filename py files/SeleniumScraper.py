# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 18:32:54 2021

@author: Robin
"""
import pandas as pd
import selenium as sl
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/Users/Robin/chromedriver.exe')
driver.get('https://baseballsavant.mlb.com/daily_matchups')
stats= driver.find_elements_by_class_name('default-table-row   ')
stats_list = []
for s in range(len(stats)):
    stats_list.append(stats[s].text)



data_tuples = list(zip(stats_list[:],teams_list[1:])) # list of each players name and salary paired together
print(temp_df)

driver.close()