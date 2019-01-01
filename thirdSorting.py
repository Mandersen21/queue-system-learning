import numpy as np
import pandas as pd
from time import time
from IPython.display import display

import matplotlib.pyplot as plt
import seaborn as sns

import csv
from operator import attrgetter
from datetime import datetime

csvfileSorted = "./dataNewSorted2.csv"
    
dataset = pd.read_csv('dataNewSorted.csv')

data = dataset.iloc[:, 0:11].values
   
print(data)

# Encoding categorical data#
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
 
data[:, 6] = labelencoder_X.fit_transform(data[:, 6])
data[:, 8] = labelencoder_X.fit_transform(data[:, 8])

dataSorted = []

for index, val in enumerate(data):
    
    patient_id = val[10]
    numberInFront = 0
    
    # Split date up
    dateString = val[0].split()[0].split('-')
    timeString = val[0].split()[1].split(':')   
    startTimeQueue = datetime(int(dateString[0]), int(dateString[1]), int(dateString[2]), int(timeString[0]), int(timeString[1]), int(timeString[2]))
    
    dateString = val[1].split()[0].split('-')
    timeString = val[1].split()[1].split(':')
    endTime = datetime(int(dateString[0]), int(dateString[1]), int(dateString[2]), int(timeString[0]), int(timeString[1]), int(timeString[2]))
    
    for row in data:
        if (val[10] == row[10]):
            continue
                
        dateString = row[0].split()[0].split('-')
        timeString = row[0].split()[1].split(':')
        rowStartTime = datetime(int(dateString[0]), int(dateString[1]), int(dateString[2]), int(timeString[0]), int(timeString[1]), int(timeString[2]))
        
        dateString = row[1].split()[0].split('-')
        timeString = row[1].split()[1].split(':')
        rowEndTime = datetime(int(dateString[0]), int(dateString[1]), int(dateString[2]), int(timeString[0]), int(timeString[1]), int(timeString[2]))
        
        if (startTimeQueue < rowStartTime):
            continue
        
        #print("Comparing: " , startTimeQueue, " with ", rowEndTime)
        
        if (rowEndTime > startTimeQueue):
            numberInFront = numberInFront + 1
    
    #print("In front of patient: ", numberInFront)
    #print("        ")
    
    week = -1
    timeAtDay = -1
    triage = -1
    averageWaitingTime3 = -1
    waitingTime = -1
    
    triage = val[3]
    week = val[4]
    timeAtDay = val[5]
    code = val[6]
    age = val[7]
    track = val[8]
    waitingTime = val[9]

    if (index < 3):
        averageWaitingTime3 = val[9]
          
    if (index > 2):
        value1 = data[index-1][9]
        value2 = data[index-2][9]
        value3 = data[index-3][9]
        averageWaitingTime3 = round((int(value1) + int(value2) + int(value3)) / 3)
      
    if (triage == 'blå'):
        triage = 5
    if (triage == 'grøn'):
        triage = 4
    if (triage == 'gul'):
        triage = 3
    if (triage == 'orange'):
        triage = 2
    if (triage == 'rød'):
        triage = 1
              
    if (week == 'Mon'):
        week = 0
    if (week == 'Tue'):
        week = 1
    if (week == 'Wed'):
        week = 2
    if (week == 'Thu'):
        week = 3
    if (week == 'Fri'):
        week = 4
    if (week == 'Sat'):
        week = 5
    if (week == 'Sun'):
        week = 6
           
    #value = triage,timeAtDay,age,numberInFront,averageWaitingTime3,waitingTime
    value = startTimeQueue,endTime,triage,week,timeAtDay,age,numberInFront,averageWaitingTime3,waitingTime
    dataSorted.append(value)
    
dataSorted = sorted(dataSorted)
            
with open(csvfileSorted, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(dataSorted)

 

