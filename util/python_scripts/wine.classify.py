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

# print('Class labels', np.unique(df_wine['Class label']))

# print('\nWine data excerpt:\n\n', df_wine.head())

X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values

X_train, X_test, y_train, y_test = \
  train_test_split(X, y, test_size=0.3, random_state=0)

#############################################################################

stdsc = StandardScaler()
X_train_std = stdsc.fit_transform(X_train)
X_test_std = stdsc.transform(X_test)

########


def LOGREG():
  lr = linear_model.LogisticRegression()
  lr.fit(X_train_std, y_train)

  # print('Training accuracy:', lr.score(X_train_std, y_train))
  print('log reg score:', lr.score(X_test_std, y_test))

  # print('predictions', lr.predict(X_test_std))

  # print('actual', y_test)

def printer(predictionArray):

  c3 = 0
  arr = []

  for _ in range(len(predictionArray)):
    if (predictionArray[_] == y_test[_]):
      c3 += 1

    arr.append([*X_test[_], y_test[_], predictionArray[_]])

  # print('accuracy Linear SVC: ', c3 / len(svc_prediction))

  # print(X_test, y_test)

  print('printer accuracy', *arr, sep='\n')






def KNN():
  knn = neighbors.KNeighborsClassifier()
  knn.fit(X_train_std, y_train)
  print('knn score:', knn.score(X_test_std, y_test))

  # printer(knn.predict(X_test))



def _SVC_():
  SVC = svm.SVC()
  SVC.fit(X_train_std, y_train)
  print('svc score', SVC.score(X_test_std, y_test))

  # printer(SVC.predict(X_test_std))


def FOREST():
  forest = RandomForestClassifier(n_estimators=10000,
                                  random_state=0,
                                  n_jobs=-1)

  forest.fit(X_train, y_train)

  importances = forest.feature_importances_

  feat_labels = df_wine.columns[1:]

  indices = np.argsort(importances)[::-1]

  for f in range(X_train.shape[1]):
    print("%2d) %-*s %f" % (f + 1, 30,
                            feat_labels[indices[f]],
                            importances[indices[f]]))


def LINEAR_SVC_():
  SVC = svm.LinearSVC()
  SVC.fit(X_train_std, y_train)
  print('linear svc score', SVC.score(X_test_std, y_test))

  printer(SVC.predict(X_test_std))


LINEAR_SVC_()

# FOREST()


