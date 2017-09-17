import pandas as pd

import numpy as np

from sklearn import datasets, neighbors, linear_model, preprocessing, svm

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score

from sklearn.base import clone

from itertools import combinations

from sklearn.ensemble import RandomForestClassifier

SCALER = StandardScaler()

sc = SCALER

#############################################################################
print(50 * '=')
print('Section: Unsupervised dimensionality reduction'
      ' via principal component analysis')
print(50 * '-')

df_wine = pd.read_csv('https://archive.ics.uci.edu/'
                      'ml/machine-learning-databases/wine/wine.data',
                      header=None)

df_wine.columns = ['Class label', 'Alcohol', 'Malic acid', 'Ash',
                   'Alcalinity of ash', 'Magnesium', 'Total phenols',
                   'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
                   'Color intensity', 'Hue', 'OD280/OD315 of diluted wines',
                   'Proline']

print('Class labels', np.unique(df_wine['Class label']))

print('\nWine data excerpt:\n\n', df_wine.head())

X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values

X_train, X_test, y_train, y_test = \
  train_test_split(X, y, test_size=0.3, random_state=0)

#############################################################################

stdsc = StandardScaler()
X_train_std = stdsc.fit_transform(X_train)
X_test_std = stdsc.transform(X_test)

########

wine_x_train = X_train
wine_x_test = X_test

wine_x_train_std = X_train_std
wine_x_test_std = X_test_std

wine_y_train = y_train
wine_y_test = y_test


def LOGREG():
  # blank score = 0.65
  lr = linear_model.LogisticRegression(C=0.1, penalty='l1')
  lr.fit(wine_x_train, wine_y_train)

  print('Training accuracy:', lr.score(X_train_std, y_train))
  print('Test accuracy:', lr.score(X_test_std, y_test))
  # print('Intercept:', lr.intercept_)
  # print('Model weights:', lr.coef_)

  print('predictions', lr.predict(X_test_std))

  print('actual', y_test)




  # print('predict_proba', logReg.predict_proba(wine_x_test_std))


def KNN():
  knn = neighbors.KNeighborsClassifier()
  knn.fit(wine_x_train, wine_y_train)
  print('knn score:', knn.score(wine_x_test_std, wine_y_test))


# print(knn.predict_proba(wine_x_test))

def MAKE_SVC():
  SVC = svm.SVC()
  SVC.fit(wine_x_train, wine_y_train)
  print('svc score', SVC.score(wine_x_test_std, wine_y_test))


def FOREST():
  forest = RandomForestClassifier(n_estimators=10000, random_state=0, n_jobs=-1)

  forest.fit(X_train, y_train)

  importances = forest.feature_importances_

  feat_labels = df_wine.columns

  arr = [[feat_labels[i], importances[i] * 100] for i in range(len(importances))]

  _sorted = sorted(arr, key=lambda i: i[1], reverse=True)

  indices = np.argsort(importances)[::-1]

  for f in range(X_train.shape[1]):
    print("%2d) %-*s %f" % (f + 1, 30,
                            feat_labels[indices[f]],
                            importances[indices[f]]))


# KNN()

# MAKE_SVC()


LOGREG()

FOREST()
