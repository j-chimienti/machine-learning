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

whiteWineUrl = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'

redWineUrl = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'

url = redWineUrl


wineQualityData = pd.read_csv(url, header=0, sep=';')

# print(wineQualityData.head())

X = wineQualityData.iloc[:, :-1].values

# get last col
y = wineQualityData.iloc[:, -1].values


X_train, X_test, y_train, y_test = \
  train_test_split(X, y, test_size=0.3, random_state=0)


X_train_std = SCALER.fit_transform(X_train)

X_test_std = SCALER.transform(X_test)


def LOGREG():
    logReg = linear_model.LogisticRegression(C = 0.1, penalty = 'l1')
    logReg.fit(X_train_std, y_train)

    print('Training accuracy:', logReg.score(X_train_std, y_train))
    print('Test accuracy:', logReg.score(X_test_std, y_test))
    print('Intercept:', logReg.intercept_)
    print('Model weights:', logReg.coef_)

def KNN():
    knn = neighbors.KNeighborsClassifier()
    knn.fit(X_train_std, y_train)
    print('knn score:', knn.score(X_test_std, y_test))


# print(knn.predict_proba(X_test))

def MAKE_SVC():
    SVC = svm.SVC()
    SVC.fit(X_train_std, y_train)
    print('svc score', SVC.score(X_test_std, y_test))


def FOREST():
    feat_labels = wineQualityData.columns[:-1]

    forest = RandomForestClassifier(n_estimators=10000,
                                    random_state=0,
                                    n_jobs=-1)

    forest.fit(X_train, y_train)
    importances = forest.feature_importances_

    indices = np.argsort(importances)[::-1]

    for f in range(X_train.shape[1]):
        print("%2d) %-*s %f" % (f + 1, 30, feat_labels[indices[f]], importances[indices[f]]))



KNN()

MAKE_SVC()

LOGREG()

FOREST()

