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

#with open("./dataNewSortedWithFast.csv") as f:
#    reader = csv.reader(f)
    
dataset = pd.read_csv('test2.csv')

data = dataset.iloc[:, 0:8].values

