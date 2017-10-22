from sklearn.ensemble import RandomForestClassifier

from sklearn import neighbors, linear_model, preprocessing, svm

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

import numpy as np

from halo import Halo

spinner = Halo(text="Calculating Feature Importance", spinner='dots')

SCALER = StandardScaler()

svc = svm.LinearSVC()

KNN = neighbors.KNeighborsClassifier()

logistic = linear_model.LogisticRegression(C=1e5)


class Classify():
  '''


    @param X Array<any>
    @param y Array<String>
    @param columns Array<String>


  '''

  def __init__(self, X, y, standardizeData=False, types=['KNN', 'svc', 'log'], columns=None):

    self.forest = RandomForestClassifier(n_estimators=10000,
                                         random_state=0,
                                         n_jobs=-1)

    self.importances = None

    self.columns = columns

    self.standardizeData = standardizeData

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

    self.main(X, y, types)

  def main(self, X, y, types):

    self.splitTestData(X, y)

    if self.standardizeData:
      self.standardize()

    for _ in range(len(types)):
      type = types[_]

      self.fitAndPredict(type)

      self.scores[type] = self.score(type)

    self.printComparison()

    self.run_forest()

    if self.columns:
      self.print_feature_importances()

      # return self.scores

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

    x_test = self.X_test if not self.standardizeData else self.X_test_std

    return classifier.score(x_test, self.y_test)

  def fitAndPredict(self, type):

    assert (type)

    x_train = self.X_train if not self.standardizeData else self.X_train_std

    x_test = self.X_test if not self.standardizeData else self.X_test_std

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

    print('### Classifier Juxtaposition')

    print('')

    print('KNN | Logistic Regression | Linear SVC')

    print('--- | ------------------- | --------- |')

    # print('% .4f' % self.scores['KNN'])


    print(' {:f} | {:f} | {:f}'.format(self.scores['KNN'], self.scores['log'], self.scores['svc']))

  def standardize(self):

    self.X_train_std = SCALER.fit_transform(self.X_train)

    self.X_test_std = SCALER.transform(self.X_test)

  def run_forest(self):

    spinner.start()

    self.forest.fit(self.X_train, self.y_train)

    spinner.stop()

    return True

  def print_feature_importances(self):

    feature_importances_ = self.forest.feature_importances_

    sortedFeatures = np.argsort(feature_importances_)[::-1]

    print('')

    print('*Feature Importance*')

    print(' | Feature | Importance')

    print('--- | -------- | ---------')

    num = 0

    for i in sortedFeatures:
      num += 1
      print('{} | {} | {:f}'.format(num, self.columns[i], float(feature_importances_[i])))

    print('')
