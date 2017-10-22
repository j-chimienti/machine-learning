import pandas as pd

import numpy as np

from sklearn import datasets, neighbors, linear_model, preprocessing, svm

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score

from sklearn.base import clone

from itertools import combinations

from sklearn.ensemble import RandomForestClassifier


from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error


from classify import Classify


housing = datasets.load_boston()


columns = ['CRIM', 'ZN', 'INDUS', 'CHAS',
              'NOX', 'RM', 'AGE', 'DIS', 'RAD',
              'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']


X = housing.data

y = housing.target
xx =  X # [x[5] for x in X]

DataFrame = pd.DataFrame(xx)

DataFrame.columns = columns # ['RM']


X = DataFrame.iloc[:, :-1].values
y_ = DataFrame['MEDV'].values

Classify(X, y, standardizeData = True, types = ['log'])



