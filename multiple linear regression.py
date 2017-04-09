# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 23:16:58 2017

@author: SiddheshPisal
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

#Categorical to numeric labels
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x = LabelEncoder()
X[:, 3] = labelencoder_x.fit_transform(X[:,3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

#avoid dummy trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#Fitting a linear regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Predicting test results
y_pred = regressor.predict(X_test)

#Building optimal model using Backward Elimination

import statsmodels.formula.api as sm
X = np.append(arr = np.ones((50,1)).astype(int), values = X, axis = 1)
X_opt = X[:, [0,1,2,3,4,5]]
regressor_ols = sm.OLS(endog = y, exog = X_opt).fit()
regressor_ols.summary()

X_opt = X[:, [0,1,3,4,5]]
regressor_ols1 = sm.OLS(endog = y, exog = X_opt).fit()
regressor_ols1.summary()

X_opt = X[:, [0,3]]
regressor_ols1 = sm.OLS(endog = y, exog = X_opt).fit()
regressor_ols1.summary()