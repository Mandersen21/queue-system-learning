#%matplotlib inline

import numpy as np
import pandas as pd
from time import time
from IPython.display import display

import matplotlib.pyplot as plt
import seaborn as sns

import visuals as vs

# Load the Red Wines dataset
data = pd.read_csv("./dataNewSorted.csv", sep=',')

# Patient knowledge
totalPatient = data.shape[0]
print('Total number of patients:', totalPatient)

triage_at_1 = data.loc[(data['triage'] == 1)]
triage_1_patients = triage_at_1.shape[0]
#print(triage_1_patients)

triage_at_2 = data.loc[(data['triage'] == 2)]
triage_2_patients = triage_at_2.shape[0]
#print(triage_2_patients)

triage_at_3 = data.loc[(data['triage'] == 3)]
triage_3_patients = triage_at_3.shape[0]
#print(triage_3_patients)

triage_at_4 = data.loc[(data['triage'] == 4)]
triage_4_patients = triage_at_4.shape[0]
#print(triage_4_patients)

triage_at_5 = data.loc[(data['triage'] == 5)]
triage_5_patients = triage_at_5.shape[0]
#print(triage_5_patients)

# Patient percentages
percent_triage_1 = triage_1_patients*100/totalPatient
print('Percentage triage 1:', percent_triage_1)

percent_triage_2 = triage_2_patients*100/totalPatient
print('Percentage triage 2:', percent_triage_2)

percent_triage_3 = triage_3_patients*100/totalPatient
print('Percentage triage 3:', percent_triage_3)

percent_triage_4 = triage_4_patients*100/totalPatient
print('Percentage triage 4:', percent_triage_4)

percent_triage_5 = triage_5_patients*100/totalPatient
print('Percentage triage 5:', percent_triage_5)


# Day knowledge
day_monday = data.loc[(data['weekDay'] == 0)]
total_monday = day_monday.shape[0]

day_tuesday = data.loc[(data['weekDay'] == 1)]
total_tuesday = day_tuesday.shape[0]

day_wednesday = data.loc[(data['weekDay'] == 2)]
total_wednesday = day_wednesday.shape[0]

day_thursday = data.loc[(data['weekDay'] == 3)]
total_thursday = day_thursday.shape[0]

day_friday = data.loc[(data['weekDay'] == 4)]
total_friday = day_friday.shape[0]

day_saturday = data.loc[(data['weekDay'] == 5)]
total_saturday = day_saturday.shape[0]

day_sunday = data.loc[(data['weekDay'] == 6)]
total_sunday = day_sunday.shape[0]

print(48.952879581151834 + 6.399834665197024 + 34.451639570129515 + 5.731606503168917 + 4.464039680352714)

print()

# Day percentages
print('Percentage monday:', total_monday*100/totalPatient)

print('Percentage tuesday:', total_tuesday*100/totalPatient)

print('Percentage wednesday:', total_wednesday*100/totalPatient)

print('Percentage thursday:', total_thursday*100/totalPatient)

print('Percentage friday:', total_friday*100/totalPatient)

print('Percentage saturday:', total_saturday*100/totalPatient)

print('Percentage sunday:', total_sunday*100/totalPatient)

print( 14.277349131992285 + 14.363461008542298 + 13.771011297878204 + 14.108569853954258 + 13.492008817856158 + 15.011022320198402 + 14.976577569578396)

# Visualize skewed continuous features of original data
#vs.distribution(data, "weekDay")

# Day knowledge
t_duration_1 = data.loc[(data['treatmentDuration'] == 0)]
total_monday = day_monday.shape[0]

print(data['treatmentDuration'].max())


fixedAcidity_citricAcid = data[['triage', 'treatmentDuration']]
g = sns.JointGrid(x="triage", y="treatmentDuration", data=data, size=6)
g = g.plot_joint(sns.regplot, scatter_kws={"s": 10})
g = g.plot_marginals(sns.distplot)