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

csv = __import__('wine-classify.csv')

wineQualityData = pd.read_csv(csv, header=0, sep=',')

# print(wineQualityData.head())

wine_x = wineQualityData.iloc[:, :-1]

# get last col
wine_y = wineQualityData.iloc[:, -1].values

_num = int(len(wine_x) * 0.7)

wine_x_train = wine_x[:_num]

wine_y_train = wine_y[:_num]

wine_x_test = wine_x[_num:]

wine_y_test = wine_y[_num:]

# wine_x_train, wine_y_train, wine_x_test, wine_y_test = train_test_split(wine_x, wine_y, test_size = 0.33)

wine_x_train_std = SCALER.fit_transform(wine_x_train)

wine_x_test_std = SCALER.transform(wine_x_test)


def LOGREG():
    logReg = linear_model.LogisticRegression(max_iter=1000)
    logReg.fit(wine_x_train_std, wine_y_train)
    print('score', logReg.score(wine_x_test_std, wine_y_test))

    bb = logReg.predict(wine_x_test_std)

    print('predict', *bb)

    print('quality', *wine_y_test)

    print('predict_proba', logReg.predict_proba(wine_x_test))


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

    forest.fit(wine_x_test_std, wine_y_test)

    importances = forest.feature_importances_

    feat_labels = wineQualityData.columns[:]

    arr = [[feat_labels[i], importances[i] * 100] for i in range(len(importances))]

    _sorted = sorted(arr, key=lambda i: i[1], reverse=True)

    print('feature importance:', *_sorted, sep='\n')


# MAKE_SVC()

FOREST()

# LOGREG()
