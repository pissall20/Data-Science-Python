# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 00:02:16 2017

@author: SiddheshPisal
"""

#Polynomial Regression

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
"""

#Fitting a linear regression model
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X, y)

#Fitting a polynomial model
from sklearn.preprocessing import PolynomialFeatures
polyreg = PolynomialFeatures(degree = 4)
X_poly = polyreg.fit_transform(X)

linreg2 = LinearRegression()
linreg2.fit(X_poly, y)

#Visualize the results of linear regression model
plt.scatter(X, y, color = 'red')
plt.plot(X, linreg.predict(X), color = 'blue')
plt.title('Salaries of positions')
plt.ylabel('Salary')
plt.xlabel('Position')
plt.show()

#Visualize the results of polynomial regression model
#X_grid = np.arange(min(X),max(X), 0.1)
#X_grid = X_grid.reshape((len(X_grid),1))
plt.scatter(X, y, color = 'red')
plt.plot(X, linreg2.predict(polyreg.fit_transform(X)), color = 'blue')
plt.title('Salaries of positions')
plt.ylabel('Salary')
plt.xlabel('Position')
plt.show()

#Predicting with linear reg
linreg.predict(6.5)

#Prediciting with polynomial reg
linreg2.predict(polyreg.fit_transform(6.5))