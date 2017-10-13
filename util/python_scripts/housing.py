import pandas as pd

import numpy as np

from sklearn import datasets, neighbors, linear_model, preprocessing, svm

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score

from sklearn.base import clone

from itertools import combinations

from sklearn.ensemble import RandomForestClassifier

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
y = DataFrame['MEDV'].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0)

sc_x = StandardScaler()
sc_y = StandardScaler()
#X_std = sc_x.fit_transform(X)
#y_std = sc_y.fit_transform(y[:, np.newaxis]).flatten()

slr = linear_model.LinearRegression()

slr.fit(X_train, y_train)

y_train_pred = slr.predict(X_train)
y_test_pred = slr.predict(X_test)

print('slope %.3f' % slr.coef_[0])


print('Intercept: %.3f' % slr.intercept_)


from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

print('MSE train: %.3f, test: %.3f' % (
        mean_squared_error(y_train, y_train_pred),
        mean_squared_error(y_test, y_test_pred)))
print('R^2 train: %.3f, test: %.3f' % (
        r2_score(y_train, y_train_pred),
        r2_score(y_test, y_test_pred)))
