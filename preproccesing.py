import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import explained_variance_score
from sklearn.metrics import r2_score
from scipy.stats import spearmanr, pearsonr

#Data loading 
dataset = pd.read_csv('dataNewSorted.csv')

# Without date
X = dataset.iloc[:, 0:3].values

A = [1,0,0,1,0,0,0,0,0,0,7]
B = [1,0,0,1,0,0,0,0,0,0,15]
C = [0,0,1,1,0,0,0,0,0,0,7]
D = [0,0,1,1,0,0,0,0,0,0,15]

# With date
#X2 = dataset.iloc[:, 0:6].values

y = dataset.iloc[:, 3].values

# Encoding categorical data#
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
X[:, 1] = labelencoder_X.fit_transform(X[:, 1])
X[:, 2] = labelencoder_X.fit_transform(X[:, 2])
#X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
#X[:, 4] = labelencoder_X.fit_transform(X[:, 4])

onehotencoder = OneHotEncoder(categorical_features = [0,1])
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

# Fitting Random Forest Regression to the dataset
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators=10, oob_score=True, random_state=0)
rf.fit(X_train, y_train)

# Predicting a new result
predicted_train = rf.predict(X_train)
predicted_test = rf.predict(X_test)

#print('Predicting blue morgen: ',rf.predict([A]))
#print('Predicting blue eftermiddag: ',rf.predict([B))
print('Predicting gul morgen: ',rf.predict([C]))
#print('Predicting gul eftemiddag: ',rf.predict([D]))

#print(accuracy_score(y_pred, y))
#print(explained_variance_score(y_test, y_pred))

#test_score = r2_score(y_test, predicted_test)
#spearman = spearmanr(y_test, predicted_test)
#pearson = pearsonr(y_test, predicted_test)
#print(f'Out-of-bag R-2 score estimate: {rf.oob_score_:>5.3}')
#print(f'Test data R-2 score: {test_score:>5.3}')
#print(f'Test data Spearman correlation: {spearman[0]:.3}')
#print(f'Test data Pearson correlation: {pearson[0]:.3}')
