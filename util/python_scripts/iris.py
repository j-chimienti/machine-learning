import pandas as pd

import numpy as np

from sklearn import datasets, neighbors, linear_model, preprocessing, svm

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score

from sklearn.base import clone

from itertools import combinations

from sklearn.ensemble import RandomForestClassifier


# Create and fit a nearest-neighbor classifier
from sklearn.neighbors import KNeighborsClassifier

#############################################################################
print(50 * '=')
print('Section: Unsupervised dimensionality reduction'
      ' via principal component analysis')
print(50 * '-')

iris = datasets.load_iris()

X = iris.data

y = iris.target


columns = [
  'Sepal length', 'Sepal width', "Petal length", "Petal width"
]


'''
np.random.seed(0)
indices = np.random.permutation(len(X))
X_train = X[indices[:-10]]
y_train = y[indices[:-10]]
X_test  = X[indices[-10:]]
y_test  = y[indices[-10:]]

'''


X_train, X_test, y_train, y_test = \
  train_test_split(X, y, test_size=0.3, random_state=0)



_estimator = KNeighborsClassifier()

_estimator.fit(X_train, y_train)

pred_knn = _estimator.predict(X_test)

acc = 0

for _ in range(len(pred_knn)):
  if (pred_knn[_] == y_test[_]):
    acc += 1

print('K Neighbors Accuracy', acc / len(y_test))




logistic = linear_model.LogisticRegression(C= 1e5)

logistic.fit(X_train, y_train)

pred2 = logistic.predict(X_test)

c2 = 0

for _ in range(len(pred2)):
  if (pred2[_] == y_test[_]):
    c2 += 1

print('Logistic Regression Accuracy: ', c2 / len(pred2))




print('pred log Reg', pred2)

svc = svm.LinearSVC()

svc.fit(X_train, y_train)

svc_prediction = svc.predict(X_test)

c3 = 0

arr = []

for _ in range(len(pred_knn)):
  if (pred_knn[_] == y_test[_]):
    c3 += 1

  arr.append([*X_test[_], y_test[_], pred_knn[_]])

print('accuracy Linear SVC: ', c3 / len(svc_prediction))

# print(X_test, y_test)

print('knn accuracy', *arr, sep = '\n')



def FOREST():
  forest = RandomForestClassifier(n_estimators=10000,
                                  random_state=0,
                                  n_jobs=-1)

  forest.fit(X_train, y_train)

  importances = forest.feature_importances_

  feat_labels = columns

  indices = np.argsort(importances)[::-1]

  for f in range(X_train.shape[1]):
    print("%2d) %-*s %f" % (f + 1, 30,
                            feat_labels[indices[f]],
                            importances[indices[f]]))


FOREST()

