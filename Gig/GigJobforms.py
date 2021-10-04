# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 15:12:26 2021
Handy Wo-Man service, gig worker application for recording all information about a gig/job.
**info from job record upon receival**
-Date booked-X
-Date of Service-X
-Time of Service-X
-estimated duration
-address/city/state
-client name
-rate 
-service type(cleaning, repairs)
Source of booking(app, referal HH client,etc)
Job#
Directive/Goal(moveout clean, leaking sink,etc)
Size
quantity
condition
notes-X
equipment
purchases
**Info that must be entered upon completion of job***
actual Start & Finish
Actual paid$
Reimbursemtn
Tip
Date Paid
Directive fully acheived?(if no-notes for remaining work)
Additional actions(mail card, schedule next appt. etc)
Mileage 
Allocated Purchase
Notes for Record


all this saved in a xls format
@author: Robin C. Hoffpauir
"""

from tkinter import *
from tkinter import ttk
Root = Tk()
Root.title('New Job/Gig Details')
root = Toplevel(Root)






mainframe=ttk.Frame(root)
mainframe.grid(column=4,row=20,sticky=(N, W, E, S))
mainframe['relief']='sunken'
root.columnconfigure(0,weight=1)
root.rowconfigure(0, weight=1)
c=Canvas(root)

    

date_booked=StringVar()
date_service=StringVar()
time_service=StringVar()


date_booked = ttk.Entry(mainframe, width=9,textvariable=date_booked)
time_service = ttk.Entry(mainframe, width = 9, textvariable=time_service)
date_service = ttk.Entry(mainframe, width = 9, textvariable=date_service)
job_notes = ttk.Entry(mainframe, width = 50, foreground='blue',background='gray')
directive = ttk.Entry(mainframe, width = 50, foreground='blue',background='gray')
equipment = ttk.Entry(mainframe, width=50, foreground='blue',background='gray')

date_booked.grid(column=2,row=1,sticky=(W,E))
date_service.grid(column=4,row=1,sticky=(W,E))
time_service.grid(column= 2,row=3,sticky=(W,E))
job_notes.grid(column = 2,row = 14,sticky=(W,E))
directive.grid(column = 2,row = 10,sticky=(W,E))
equipment.grid(column=2, row=15,sticky=(W,E))





ttk.Label(mainframe,text='Date Booked').grid(column=1,row=1,sticky=(W,E))
ttk.Label(mainframe,text='Date of Service').grid(column=3,row=1,sticky=(W,E))
ttk.Label(mainframe,text='Time of Service').grid(column=1,row=3,sticky=(W,E))
ttk.Label(mainframe,text='Duration(estimate)').grid(column=1,row=4,sticky=(W,E))
ttk.Label(mainframe,text='Address/City/State').grid(column=1,row=5,sticky=(W,E))
ttk.Label(mainframe,text='Client Name').grid(column=1,row=6,sticky=(W,E))
ttk.Label(mainframe,text='Rate').grid(column=1,row=7,sticky=(W,E))
ttk.Label(mainframe,text='Service Type').grid(column=1,row=8,sticky=(W,E))
ttk.Label(mainframe,text='Job #').grid(column=1,row=9,sticky=(W,E))
ttk.Label(mainframe,text='Directive/Goal').grid(column=1,row=10,sticky=(W,E))
ttk.Label(mainframe,text='Size').grid(column=1,row=11,sticky=(W,E))
ttk.Label(mainframe,text='Quantity').grid(column=1,row=12,sticky=(W,E))
ttk.Label(mainframe,text='Condition').grid(column=1,row=13,sticky=(W,E))
ttk.Label(mainframe,text='Notes').grid(column=1,row=14,sticky=(W,E))
ttk.Label(mainframe,text='Equipment').grid(column=1,row=15,sticky=(W,E))
ttk.Label(mainframe,text='Purchases').grid(column=1,row=16,sticky=(W,E))






def getinput():  
    equipment_text = equipment.get('1.0')
    directive_text = job_notes.get('1.0')
    job_notes_text = job_notes.get('1.0')
 

    global params
    params = [equipment_text, directive_text, job_notes_text]
    
Button(mainframe, text = "submit", command =getinput).grid(row=20, sticky=(W,E))


root.mainloop()