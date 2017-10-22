import numpy as np

from sklearn.ensemble import RandomForestClassifier

from sklearn import neighbors, linear_model, preprocessing, svm

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

import sys

SCALER = StandardScaler()

svc = svm.LinearSVC()

KNN = neighbors.KNeighborsClassifier()

logistic = linear_model.LogisticRegression(C=1e5)


class Classify():
  def __init__(self, X, y, standardizeData = False, types=['KNN', 'svc', 'log']):

    self.forest = RandomForestClassifier(n_estimators=10000,
                                         random_state=0,
                                         n_jobs=-1)

    classifiers = {}
    classifiers['KNN'] = KNN
    classifiers["log"] = logistic
    classifiers["svc"] = svc

    self.classifiers = classifiers

    fitData = {}

    fitData['KNN'] = None
    fitData['log'] = None
    fitData['svc'] = None

    self.fitData = fitData

    predictions = {}

    predictions['KNN'] = None
    predictions['log'] = None
    predictions['svc'] = None

    self.predictions = predictions

    self.X_train = None
    self.X_test = None
    self.y_train = None
    self.y_test = None

    self.X_train_std = None

    self.X_test_std = None

    scores = {}

    scores['KNN'] = None
    scores['log'] = None
    scores['svc'] = None

    self.scores = scores

    self.main(X, y, types, standardizeData)

  def main(self, X, y, types, standardizeData):
    self.splitTestData(X, y)

    if standardizeData:
      self.standardizeData()

    for _ in range(len(types)):
      type = types[_]

      self.fitAndPredict(type, standardizeData)

      self.scores[type] = self.score(type)

    self.printComparison()

    return self.scores

  def splitTestData(self, X, y):
    X_train, X_test, y_train, y_test = \
      train_test_split(X, y, test_size=0.3, random_state=0)

    self.X_train = X_train

    self.X_test = X_test

    self.y_train = y_train

    self.y_test = y_test

  def assertValidType(self, type):
    assert (type == 'KNN' or type == 'log' or type == 'svc')

  def score(self, type):
    classifier = self.classifiers[type]

    return classifier.score(self.X_test, self.y_test)


  def fitAndPredict(self, type, standardizeData):

    assert(type)

    x_train = self.X_train if not standardizeData else self.X_train_std

    x_test = self.X_test if not standardizeData else self.X_test_std

    y = self.y_train

    self.fit(x_train, y, type)

    self.predict(x_test, type)

  def fit(self, X_train, y_train, type="KNN"):
    self.assertValidType(type)

    classifier = self.classifiers[type]

    self.fitData[type] = classifier.fit(X_train, y_train)

  def predict(self, X_test, type="KNN"):
    self.assertValidType(type)

    classifier = self.classifiers[type]

    self.predictions[type] = classifier.predict(X_test)

  def printComparison(self):

    print('### Classification accuracy comparison')

    print('This table compares the results of the 3 algorithms that were used to classify'
          ' wine data.'
          )

    print('KNN | Logistic Regression | Linear SVC')

    print('--- | ------------------- | --------- |')



    # print('% .4f' % self.scores['KNN'])


    print(' {} | {} | {}'.format(self.scores['KNN'], self.scores['log'], self.scores['svc']))



  def standardizeData(self):



    self.X_train_std = SCALER.fit_transform(self.X_train)

    self.X_test_std = SCALER.transform(self.X_test)

  def FOREST(self):

    self.forest.fit(self.X_train, self.y_train)

    importances = self.forest.feature_importances_

    #  feat_labels = df_wine.columns[1:]

    # indices = np.argsort(importances)[::-1]

    for f in range(self.X_train.shape[1]):
      print(f)

      # print("%2d) %-*s %f" % (f + 1, 30,
      #                      feat_labels[indices[f]],
      #                      importances[indices[f]]))
