# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 00:09:40 2021

@author: Robin
"""

import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
import csv

pd.options.display.max_rows=None
pd.options.display.max_columns=None
gig_prelim=pd.DataFrame(columns=['Yes','No','Particulars'])