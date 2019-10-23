# FSIQ - IK, MRI_Count - brainsize

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('data', sep=" ", header=None)

X = data.iloc[:,1]
Y = data.iloc[:,6]
X_training = X[:30]
Y_training = Y[:30]
X_test = X[30:]
Y_test = Y[30:]

#regression model Y = m*X+cprint(cost
m = 0
c = 0
L = 0.0000001 #spusk
counter = 100000 # amount of steps

n = float(len(X_training))
for i in range(counter):
    prediction = (m*X_training)+c
    cost = sum([i**2 for i in (Y_training-prediction)])



    mg = -(2/n) * sum(X_training*(Y_training-prediction))

    cg = -(2/n) * sum(Y_training-prediction)

    m = m - (L*mg)
    c = c - (L*cg)
X_predicted = X_test*m+c
print(m,c)
error = X_predicted-Y_test
print(error)
