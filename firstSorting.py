import csv
from operator import attrgetter
from datetime import datetime
from operator import itemgetter

def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list

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
    
    fromDate = datetime(2017, 7, 1)
    
    for row in reader:
        if ((len(row[16]) > 0) and 'AHH AKAHVH' in row[10] and len(row[5]) > 0 and len(row[3]) > 0 and len(row[4]) > 0):
            
            dateString = row[3].split()[0].split('/')
            currentDate = datetime(int(dateString[0]), int(dateString[1]), int(dateString[2]))
            
            if (currentDate > fromDate):
                
                patientId = row[0]
                patientAge = row[1]
                
                start = row[3]
                end = row[4]
                actionCode = row[5]
                eventType = row[7]
                eventTime = row[8]
                eventDuration = row[9]
                eventRoom = row[10]
                eventTimeEnd = row[12]
                triage = row[16]
                track = row[2]
            
                value = patientId,patientAge,triage,actionCode,track,eventType,eventTime,eventDuration,eventRoom,start,end
                data.append(value)
                    
    dataSorted = sorted(data, key=itemgetter(0,6))
               
    with open(csvfileSorted, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(dataSorted) 