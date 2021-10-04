# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 23:20:02 2021

@author: Robin
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd
import pybaseball as pyb 

def calculate(*args):
    try:
        value=float(feet.get())
        meters.set(int(0.3048*value*10000+0.5)/10000.0)
    except ValueError:
        pass
root=Tk()
root.title('New Job Entry Form')

mainframe=ttk.Frame(root,padding='3 3 12 12')
mainframe.grid(column=2,row=3,sticky=(N, W, E, S))
root.columnconfigure(0,weight=1)
root.rowconfigure(0, weight=1)

feet=StringVar()
feet_entry=ttk.Entry(mainframe,width=9,textvariable=feet)
feet_entry.grid(column=1,row=1,sticky=(W,E))

meters=StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2,row=3,sticky=(W,E))

ttk.Button(mainframe,text='Calculate',command=calculate).grid(column=2,row=2,sticky=W)

ttk.Label(mainframe,text='feet').grid(column=2,row=1,sticky=(W,E))
ttk.Label(mainframe,text='is equivalent to').grid(column=1,row=3,sticky=S)
ttk.Label(mainframe,text='meters').grid(column=3,row=3,sticky=E)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
    
feet_entry.focus()
root.bind('<Return>',calculate)

root.mainloop()
help()