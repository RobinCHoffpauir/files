# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 22:26:37 2021

@author: Robin
"""

# importing required modules
from zipfile import ZipFile

# specifying the zip file name
file_name = "C:/Users/Robin/BayouBobsProject/BayouBobs/Bayoubobs.zip"

# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()

    # extracting all the files
    print('Extracting all the files now...')
    file = zip.extractall()
    print('Done!')
