import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Data loading 
dataset = pd.read_csv('dataNewSorted.csv')

# Without date
X = dataset.iloc[:, 1:6].values

# With date
#X2 = dataset.iloc[:, 0:6].values

y = dataset.iloc[:, 6].values

# Encoding categorical data#
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 1] = labelencoder_X.fit_transform(X[:, 1])
X[:, 2] = labelencoder_X.fit_transform(X[:, 2])
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
X[:, 4] = labelencoder_X.fit_transform(X[:, 4])

onehotencoder = OneHotEncoder(categorical_features = [1,2,3,4])
X = onehotencoder.fit_transform(X).toarray()

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

sc_y = StandardScaler()
y_train = y_train.reshape(-1, 1)
y_train = sc_y.fit_transform(y_train)
y_test = y_test.reshape(-1, 1)
y_test = sc_y.transform(y_test)