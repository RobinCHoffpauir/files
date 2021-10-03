# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 18:32:54 2021

@author: Robin
"""
import pandas as pd
import selenium as sl
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/Users/Robin/chromedriver.exe')
driver.get('https://www.baseball-reference.com/leagues/majors/2021.shtml')
stats= driver.find_elements_by_xpath('//td[@class="right "]')
stats_list = []
for s in range(len(stats)):
    stats_list.append(stats[s].text)

teams = driver.find_elements_by_xpath('//td[@class="left "]')
teams_list = []
for t in range(len(teams)):
    teams.append(teams[t].text)

data_tuples = list(zip(stats_list[:],teams_list[1:])) # list of each players name and salary paired together
temp_df = pd.DataFrame(data_tuples, columns=['#Bat','BatAge','R/G','G','PA','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','SO','BA','BP','SLG','OPS','OPS+','TB','GDP','HBP','SH','SF','IBB','LOB']) # creates dataframe of each tuple in list
print(temp_df)

driver.close()