# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 23:55:01 2021

@author: Robin
"""
import pyodbc

conn_str=(r'Driver={Mivrosoft Access Driver (*.mdb,*accdb)};'

r' DBQ=D:\Parlayking_BB_MLBData\mlbstats_be.accdb;')
conn=pyodbc.connect(conn_str)
cursor=conn.cursor()
cursor.execute('select * from Batting')

for row in cursor.fetchall():
    print(row)