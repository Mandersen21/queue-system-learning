import numpy as np
import pandas as pd
from time import time
from IPython.display import display

import matplotlib.pyplot as plt
import seaborn as sns

import csv
from operator import attrgetter
from datetime import datetime

#import visuals as vs

#matplotlib inline

csvfileSorted = "./dataNewSorted.csv"

with open("./dataNew.csv") as f:
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
                
                if (triage == 'orange'):
                    regular_duration = 0
                if (triage == 'rÃ¸d'):
                    regular_duration = 0
                
                #value = start,age,triage,date,code,triage_duration,regular_duration,fasttrack_duration,treatment_duration,end
                #value = age,triage,date,timeOfDay,track,regular_duration
                value = flytind,flytud,end,triage,date,int(timeOfDay),code,age,track,regular_duration,patient
                if (regular == 1 and fasttrack == 0 and triage != 'orange' and triage != 'rÃ¸d'):
                    dataSorted.append(value)

                regular_duration = 0
                fasttrack_duration = 0
                triage_duration = 0
                treatment_duration = 0
                fasttrack = 0
                regular = 0
                duration = 0
         
        if (val[8] == 'AHH AKAHVH Vente skade'):
            #print('VenteSkade: ', val[7])
            regular_duration = int(val[7]) + int(regular_duration)
            regular = 1
            patient = val[0]
            
            if (val[5] == 'FLYT IND'):
                flytind = val[6]
                
            if (val[5] == 'FLYT UD'):
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
            #value = start,age,triage,dayOfWeek.weekday(),code,triage_duration,regular_duration,fasttrack_duration,treatment_duration,end
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
            
            if (triage == 'orange'):
                regular_duration = 0
            if (triage == 'rÃ¸d'):
                regular_duration = 0
            
            #value = age,triage,date,timeOfDay,track,regular_duration
            value = flytind,flytud,end,triage,date,int(timeOfDay),code,age,track,regular_duration,patient
            if (regular == 1 and fasttrack and triage != 'orange' and triage != 'rÃ¸d'):
                dataSorted.append(value)
        patientOld = patientId
    
    dataSorted = sorted(dataSorted,reverse=True)
    #dataSorted = sorted(dataSorted)
    
    with open(csvfileSorted, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(dataSorted) 