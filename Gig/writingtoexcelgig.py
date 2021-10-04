# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 10:28:37 2021

@author: Robin
"""
# Writing to an excel
# sheet using Python
import xlwt
from xlwt import Workbook

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(1, 0, 'Job Number')
sheet1.write(2, 0, 'Date Booked')
sheet1.write(3, 0, 'Job Date')
sheet1.write(4, 0, '')
sheet1.write(5, 0, 'CLOCK TOWER')
sheet1.write(0, 1, 'ISBT DEHRADUN')
sheet1.write(0, 2, 'SHASTRADHARA')
sheet1.write(0, 3, 'CLEMEN TOWN')
sheet1.write(0, 4, 'RAJPUR ROAD')
sheet1.write(0, 5, 'CLOCK TOWER')

wb.save('xlwt example.xls')

