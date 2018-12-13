import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import explained_variance_score

#Data loading 
dataset = pd.read_csv('dataNewSorted.csv')

# Without date
X = dataset.iloc[:, 0:5].values

# With date
#X2 = dataset.iloc[:, 0:6].values

y = dataset.iloc[:, 5].values

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


# =============================================================================
#  # Feature Scaling
# from sklearn.preprocessing import StandardScaler
# sc_X = StandardScaler()
# X_train = sc_X.fit_transform(X_train)
# X_test = sc_X.transform(X_test)
#  
# sc_y = StandardScaler()
# y_train = y_train.reshape(-1, 1)
# y_train = sc_y.fit_transform(y_train)
# y_test = y_test.reshape(-1, 1)
# y_test = sc_y.transform(y_test)
# =============================================================================



# Fitting Random Forest Regression to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 1, random_state = 0)
regressor.fit(X_train, y_train)

# Predicting a new result
y_pred = regressor.predict(X_test)
#print(accuracy_score(y_pred, y))
print(explained_variance_score(y_test, y_pred))
# =============================================================================
# # Visualising the Random Forest Regression results (higher resolution)
# X_grid = np.arange(min(X), max(X), 0.01)
# X_grid = X_grid.reshape((len(X_grid), 1))
# plt.scatter(X, y, color = 'red')
# plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
# plt.title('Truth or Bluff (Random Forest Regression)')
# plt.xlabel('Position level')
# plt.ylabel('Salary')
# plt.show()
# =============================================================================
