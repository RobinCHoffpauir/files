import tkinter as tk
from tkinter import *
from tkinter import ttk
import xlsxwriter as xlsx

root=Tk()
root.title('New Job/Gig Details')

##define our first function
def Save():
    if B2=='active':
        file=xlsxwriter.


    
    

mainframe=ttk.Frame(root)
mainframe.grid(column=4,row=20,sticky=(N, W, E, S))
mainframe['relief']='sunken'
root.columnconfigure(0,weight=1)
root.rowconfigure(0, weight=1)
c=Canvas(root)




date_booked=StringVar()
date_booked_entry=ttk.Combobox(mainframe,width=9,textvariable=date_booked)
date_booked_entry.grid(column=2,row=1,sticky=(W,E))
date_service=StringVar()
date_service=ttk.Combobox(mainframe,width=9,textvariable=date_service)
date_service.grid(column=4,row=1,sticky=(W,E))
time_service=StringVar()
time_service=ttk.Combobox(mainframe,width=9,textvariable=date_service)
time_service.grid(column=2,row=3,sticky=(W,E))
job_notes=Text(mainframe,width=50,height=2,foreground='blue',background='gray')
job_notes_text=job_notes.get('1.0','end')
job_notes.grid(column=2,row=14)

directive=Text(mainframe,width=50,height=2,foreground='black',background='yellow')
directive_text=directive.get('1.0','end')
directive.grid(column=2,row=10)


B1=ttk.Button(mainframe,text='Save',command='saveForm').grid(column=4,row=20,sticky=W)
B2=ttk.Button(mainframe,text='Print',command='printForm').grid(column=3,row=20,sticky=W)

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



for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
    


root.mainloop()
