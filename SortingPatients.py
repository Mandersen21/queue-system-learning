import numpy as np
import pandas as pd
from time import time
from IPython.display import display

import matplotlib.pyplot as plt
import seaborn as sns

import csv
from operator import attrgetter
from datetime import datetime

# Gammel data (data.csv) 
# 0  - Patient ID
# 1  - Patient alder
# 2  - Behandlings kontakt spor
# 3  - Start tidspunkt
# 4  - Slut tidspunkt
# 5  - Aktionskode
# 6  - Ikke vigtigt
# 7  - Hændelsestype
# 8  - Hændelses tidspunkt
# 9  - Hændelsesvarighed (minutter)
# 10 - Hændelses rumnavn
# 11 - Hændelses rumnummer
# 12 - Ikke vigtigt
# 13 - Ikke vigtigt
# 14 - Ikke vigtigt
# 15 - Ikke vigtigt
# 16 - Triage

csvfileSorted = "./dataNew.csv"

with open("./data.csv") as f:
    reader = csv.reader(f)
    next(reader) # skip header
         
    data = []
    dataSorted = []
    
    patientId = '';
    patientAge = 0;
    track = 0;
    start = '';
    end = '';
    actionCode = '';
    eventType = '';
    eventTime = '';
    eventDuration = 0;
    eventRoom = '';  
    triage = -1;
    
    for row in reader:
        if ((len(row[16]) > 0) and 'AHH AKAHVH' in row[10] and len(row[5]) > 0):
                        
            patientId = row[0]
            patientAge = row[1]
            
            if ('VURDERINGSSPOR' in row[2]):
                track = 0;
            
            if ('BEHANDLERSPOR SKADE' in row[2]):
                track = 1;
            
            start = row[3]
            end = row[4]
            actionCode = row[5]
            eventType = row[7]
            eventTime = row[8]
            eventDuration = row[9]
            eventRoom = row[10]
            eventTimeEnd = row[12]
            
            if ('blÃ¥' in row[16]):
                triage = 5
            if ('grÃ¸n' in row[16]):
                triage = 4
            if ('gul' in row[16]):
                triage = 3
            if ('orange' in row[16]):
                triage = 2
            if ('rÃ¸d' in row[16]):
                triage = 1
                 
            value = patientId,patientAge,triage,actionCode,track,eventType,eventTime,eventDuration,eventRoom,start,end
            data.append(value)
                    
    dataSorted = sorted(data)
               
    with open(csvfileSorted, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(dataSorted) 