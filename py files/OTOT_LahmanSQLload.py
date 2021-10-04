# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 03:21:52 2021

@author: Robin
"""
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=OTOTS_SURFACE\OTOT;'
                      'Database=Lahman;'
                      'Trusted_Connection=yes;')
data = conn.execute('SELECT * FROM Batting WHERE yearID > 2000 AND SB > 30')


data_ = data.fetchall()
