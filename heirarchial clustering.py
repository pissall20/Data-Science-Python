# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:17:33 2017

@author: SiddheshPisal
"""

#Importing libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Import dataset
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:,[3,4]].values

#Using dendogram to find optimal number of clusters
import scipy.cluster.hierarchy as sch
dendogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title('Dendogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distance')
plt.show()

#Fitting the clustering algorithm

from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage = 'ward')
y_pred = hc.fit_predict(X)

#Visualizing the clusters

plt.scatter(X[y_pred == 0, 0],X[y_pred == 0, 1], color ='red', s = 100, label = 'Careful')
plt.scatter(X[y_pred == 1, 0],X[y_pred == 1, 1], color ='blue', s = 100, label = 'Standard')
plt.scatter(X[y_pred == 2, 0],X[y_pred == 2, 1], color ='green', s = 100, label = 'Target')
plt.scatter(X[y_pred == 3, 0],X[y_pred == 3, 1], color ='cyan', s = 100, label = 'Careless')
plt.scatter(X[y_pred == 4, 0],X[y_pred == 4, 1], color ='magenta', s = 100, label = 'Sensible')
plt.title('Clusters of customers')
plt.xlabel('Salary')
plt.ylabel('Spending Score')
plt.legend()
plt.show()