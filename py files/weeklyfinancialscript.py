# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 21:01:30 2021

@author: Robin
"""
import pandas as pd

wb = pd.read_excel('0107 Weekly Financials.xls')
wb = wb.fillna(0)
days = ['Expenses', 'Sunday', 'Monday', 'Tuesday',
        'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Total']
wb.columns = days
wb.index = wb['Expenses']
wb = wb.drop('Expenses', axis=1)
