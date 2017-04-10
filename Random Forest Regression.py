# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 21:45:03 2017

@author: SiddheshPisal
"""

#Random Forest regressor
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

#Fitting random forest regression model
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 300, random_state = 0)
regressor.fit(X,y)

#Prediction
y_pred = regressor.predict(6.5)

#Visualize the results of DT Regression model
X_grid = np.arange(min(X),max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid),1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Salaries of positions')
plt.ylabel('Salary')
plt.xlabel('Position')
plt.show()