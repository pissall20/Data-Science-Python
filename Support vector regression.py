# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 18:49:32 2017

@author: SiddheshPisal
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)


#Fitting a SVR model
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X, y)

#Prediction
y_pred = sc_y.inverse_transform(regressor.predict(sc_X.fit_transform(np.array([[6.5]]))))

#Visualize the results of SVR model
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Salaries of positions')
plt.ylabel('Salary')
plt.xlabel('Position')
plt.show()