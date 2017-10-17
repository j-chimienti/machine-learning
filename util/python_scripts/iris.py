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

iris = datasets.load_iris()

X = iris.data

y = iris.target

columns = [
  'Sepal length', 'Sepal width', "Petal length", "Petal width"
]

X_train, X_test, y_train, y_test = \
  train_test_split(X, y, test_size=0.3, random_state=0)

# Classifiers

svc = svm.LinearSVC()

svc.fit(X_train, y_train)

svc_prediction = svc.predict(X_test)

KNN = KNeighborsClassifier()

KNN.fit(X_train, y_train)

knn_prediction = KNN.predict(X_test)

logistic = linear_model.LogisticRegression(C=1e5)

logistic.fit(X_train, y_train)

logistic_predictions = logistic.predict(X_test)


def accuracy(predictions, observations):
  num_ = 0

  for _ in range(len(predictions)):

    if (predictions[_] == observations[_]):
      num_ += 1

  return num_ / len(predictions)


logistic_accuracy = accuracy(logistic_predictions, y_test)

svc_accuracy = accuracy(svc_prediction, y_test)

knn_accuracy = accuracy(knn_prediction, y_test)

print('### Classification accuracy comparison')

print('This table compares the results of the 3 algorithms that were used to classify'
      ' wine data.'
      )

print('KNN | Logistic Regression | Linear SVC')

print('--- | ------------------- | --------- |')

# print('%.4f | %.4f | %.4f' % logistic_accuracy, knn_accuracy, svc_accuracy)

print('{} | {} | {}'.format(logistic_accuracy, svc_accuracy, knn_accuracy))
