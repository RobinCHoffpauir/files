""" This Program was made by Robin C Hoffpauir on August 11th, 2021 for Gulf Breeze Pest Control"""
import datetime
import pandas as pd
date = input('What is the Day of Service?: ')
client = input('Clients Name: ')
address = input('Clients Address: ')
time = input('What time is the Job?: ')
phone = input('Clients Phone #: ')
amount = input('Amount of Service $: ')
method = input('Payment Method (Cash/Check/Callin): ')
notes = input('Customer Notes: ')
anotherentry = input('Is there another entry for this day? (Y/N): ')
if anotherentry == 'Y':
    client1 = input('Clients Name: ')
    address1 = input('Clients Address: ')
    time1 = input('What time is the Job?: ')
    phone1 = input('Clients Phone #: ')
    amount1 = input('Amount of Service $: ')
    method1 = input('Payment Method (Cash/Check/Callin): ')
    notes1 = input('Customer Notes: ')
    anotherentry1 = input('Is there another entry for this day? (Y/N): ')
else:
    Client_list = pd.DataFrame({'Client': [client], 'Address': [address], 'Time': [time], 'Phone #': [phone], 'Amount $': [amount], 'Payment Method': [method], 'Notes': [notes]})
    if anotherentry1 == 'Y':
        client2 = input('Clients Name: ')
        address2 = input('Clients Address: ')
        time2 = input('What time is the Job?: ')
        phone2 = input('Clients Phone #: ')
        amount2 = input('Amount of Service $: ')
        method2 = input('Payment Method (Cash/Check/Callin): ')
        notes2 = input('Customer Notes: ')
        anotherentry2 = input('Is there another entry for this day? (Y/N): ')
    else:
        Client_list = pd.DataFrame({'Client': [client, client1], 'Address': [address, address1], 'Time': [time, time1], 'Phone #': [phone, phone1], 'Amount $': [amount, amount1], 'Payment Method': [method, method1], 'Notes': [notes, notes1]})
Client_list.to_excel(r'ProductionReport'+str(date)+'.xlsx')
