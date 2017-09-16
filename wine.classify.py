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

df_wine = pd.read_csv('https://archive.ics.uci.edu/ml/'
                      'machine-learning-databases/wine/wine.data',
                      header=None)

df_wine.columns = ['Class label', 'Alcohol', 'Malic acid', 'Ash',
                   'Alcalinity of ash', 'Magnesium', 'Total phenols',
                   'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
                   'Color intensity', 'Hue',
                   'OD280/OD315 of diluted wines', 'Proline']

# print('Wine data excerpt:\n\n:', df_wine.head())


X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values

X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.3, random_state=0)

X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)

cov_mat = np.cov(X_train_std.T)
eigen_vals, eigen_vecs = np.linalg.eig(cov_mat)

# print('\nEigenvalues \n%s' % eigen_vals)


#############################################################################


wine_x_train = X_train
wine_x_test = X_test


wine_x_train_std = X_train_std
wine_x_test_std = X_test_std

wine_y_train = y_train
wine_y_test = y_test




def LOGREG():
    logReg = linear_model.LogisticRegression(max_iter=1000)
    logReg.fit(wine_x_train, wine_y_train)

    # print('wine_x_train', wine_x_train)
    #print('wine_x_test', wine_x_test)

    print('score', logReg.score(wine_x_test_std, wine_y_test))

    bb = logReg.predict(wine_x_test_std)

    print('predict', *bb)

    print('quality', *wine_y_test)

    #print('predict_proba', logReg.predict_proba(wine_x_test_std))


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

    feat_labels = df_wine.columns

    arr = [[feat_labels[i], importances[i] * 100] for i in range(len(importances))]

    _sorted = sorted(arr, key=lambda i: i[1], reverse=True)

    print('feature importance:', *_sorted, sep='\n')


KNN()

MAKE_SVC()


LOGREG()


FOREST()
