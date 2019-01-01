import numpy as np
import pandas as pd
from time import time
from IPython.display import display

import matplotlib.pyplot as plt
import seaborn as sns

import csv
from operator import attrgetter
from datetime import datetime, date, time, timedelta

#import visuals as vs

#matplotlib inline

csvfileSorted = "./dataNewSorted.csv"
#csvfileSorted = "./testNew2.csv"

with open("./dataNew.csv") as f:
#with open("./testNew.csv") as f:
    reader = csv.reader(f)
    #next(reader) # skip header
         
    data = []
    dataSorted = []
    patientList = []
    
    regular = 0
    fasttrack = 0
    regular_duration = 0
    fasttrack_duration = 0
    triage_duration = 0
    treatment_duration = 0
    triage = -1
    code = ''
    age = 0
    start = ''
    end = ''
    dayOfWeek = ''
    track = ''
    timeOfDay = -1
    duration = 0
    flytind = ''
    flytud = ''
    patient = ''
      
    for row in reader:
        data.append(row)
    
    dataLength = len(data)
        
    patientOld = ''

    for index, val in enumerate(data):
        
        patientId = val[0]
        
        if (patientId not in patientList):  
            patientList.append(patientId)

            if (patientOld != patientId and len(patientOld) > 0):
                #print('New patient found', index +1)
                patientList = []
                
                date = ''
                
                if (dayOfWeek.weekday() == 0):
                    date = 'Mon'
                if (dayOfWeek.weekday() == 1):
                    date = 'Tue'
                if (dayOfWeek.weekday() == 2):
                    date = 'Wed'
                if (dayOfWeek.weekday() == 3):
                    date = 'Thu'
                if (dayOfWeek.weekday() == 4):
                    date = 'Fri'
                if (dayOfWeek.weekday() == 5):
                    date = 'Sat'
                if (dayOfWeek.weekday() == 6):
                    date = 'Sun'
                
                if (len(flytind) > 0):
                    dateString = flytind.split()[0].replace('/', '-').split('-')
                    timeString = flytind.split()[1].split(':') 
                    flytind = datetime(int(dateString[0]), int(dateString[1]), int(dateString[2]), int(timeString[0]), int(timeString[1]), int(timeString[2]))
                
                if (len(flytud) > 0):
                    dateString = flytud.split()[0].replace('/', '-').split('-')
                    timeString = flytud.split()[1].split(':')   
                    flytud = datetime(int(dateString[0]), int(dateString[1]), int(dateString[2]), int(timeString[0]), int(timeString[1]), int(timeString[2]))
                
                if (regular == 1 and fasttrack == 0 and triage != 'orange' and triage != 'rÃ¸d'):
    
                    if (len(str(flytud)) == 0):
                        flytud = flytind + timedelta(minutes=int(regular_duration))
                        flytud = datetime(flytud.year, flytud.month, flytud.day, flytud.hour, flytud.minute, flytud.second)
                     
                    if (flytud > flytind):
                        value = flytind,flytud,end,triage,date,int(timeOfDay),code,age,track,regular_duration,patient
                        dataSorted.append(value)
                         
                regular_duration = 0
                fasttrack_duration = 0
                triage_duration = 0
                treatment_duration = 0
                fasttrack = 0
                regular = 0
                duration = 0
                flytind = ''
                flytud = ''
         
        if (val[8] == 'AHH AKAHVH Vente skade'):
            
            if (regular_duration == 0):
                regular_duration = int(val[7]) + int(regular_duration)
                patient = val[0]
            
            if (val[5] == 'FLYT IND' and len(flytind) == 0):  
                flytind = val[6]
                regular = 1
                
            if (val[5] == 'FLYT UD' and len(flytud) == 0):
                flytud = val[6]
            
        if (val[8] == 'AHH AKAHVH FT1'):
            #print('Fasttrack: ', val[7])
            fasttrack_duration = int(val[7]) + int(fasttrack_duration)
            fasttrack = 1
        if (val[8] == 'AHH AKAHVH Triage'):
            #print('Triage: ', val[7])
            triage_duration = int(val[7]) + int(triage_duration)
        if ('Vente skade' not in val[8] and 'FT1' not in val[8] and 'Triage' not in val[8]):
            #print('Treatment: ', val[7])
            treatment_duration = int(val[7]) + int(treatment_duration)
         
        triage = val[2]
        code = val[3]
        age = val[1]
        start = val[9]
        end = val[10]
        dateString = val[9].split()[0].split('/')
        timeString = val[9].split()[1].split(':')
        dayOfWeek = datetime(int(dateString[0]), int(dateString[1]), int(dateString[2]))
        timeOfDay = timeString[0]
        track = val[4]
        
        if (index + 1 == dataLength):
            
            date = ''
                
            if (dayOfWeek.weekday() == 0):
                date = 'Mon'
            if (dayOfWeek.weekday() == 1):
                date = 'Tue'
            if (dayOfWeek.weekday() == 2):
                date = 'Wed'
            if (dayOfWeek.weekday() == 3):
                date = 'Thu'
            if (dayOfWeek.weekday() == 4):
                date = 'Fri'
            if (dayOfWeek.weekday() == 5):
                date = 'Sat'
            if (dayOfWeek.weekday() == 6):
                date = 'Sun'
                   
            if (regular == 1 and fasttrack == 0 and triage != 'orange' and triage != 'rÃ¸d'):
                
                dateString = flytind.split()[0].replace('/', '-').split('-')
                timeString = flytind.split()[1].split(':')   
                flytind = datetime(int(dateString[0]), int(dateString[1]), int(dateString[2]), int(timeString[0]), int(timeString[1]), int(timeString[2]))
            
                if (len(flytud) > 0):
                    dateString = flytud.split()[0].replace('/', '-').split('-')
                    timeString = flytud.split()[1].split(':')   
                    flytud = datetime(int(dateString[0]), int(dateString[1]), int(dateString[2]), int(timeString[0]), int(timeString[1]), int(timeString[2]))
                
                if (len(str(flytud)) == 0):
                    flytud = flytind + timedelta(minutes=int(regular_duration))
                    flytud = datetime(flytud.year, flytud.month, flytud.day, flytud.hour, flytud.minute, flytud.second)
                          
                if (flytud > flytind):
                    value = flytind,flytud,end,triage,date,int(timeOfDay),code,age,track,regular_duration,patient
                    dataSorted.append(value)
        patientOld = patientId
    
    dataSorted = sorted(dataSorted,reverse=True)
    print(dataSorted)
    
    with open(csvfileSorted, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(dataSorted) 
