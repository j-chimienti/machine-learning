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

forest = RandomForestClassifier(n_estimators=10000,
                                random_state=0,
                                n_jobs=-1)


def classify(X, y, standardize_data=False, types=['KNN', 'svc', 'log'], columns=None):
    X_train, X_test, y_train, y_test = split_test_data(X, y)

    X_TRAIN = X_train
    X_TEST = X_test

    if standardize_data:
        X_train_std, X_test_std = standardize(X_train, X_test)
        X_TRAIN = X_train_std
        X_TEST = X_test_std

    scores = {}

    predictions = {}

    for type_ in types:
        classifier = KNN if type_ == 'KNN' else logistic if type_ == 'log' else svc if type_ == 'svc' else None

        classifier.fit(X_TRAIN, y_train)

        predictions[type_] = classifier.predict(X_TEST)

        scores[type_] = classifier.score(X_test, y_test)

    run_forest(X_TRAIN, y_train)
    display_scores(scores)


def split_test_data(X, y):
    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size=0.3, random_state=0)

    return X_train, X_test, y_train, y_test


def display_scores(scores):
    print('')

    print('### Results')

    print('')

    print('KNN     | Logistic Reg    | SVC      ')

    print('------- | --------------- | -------- ')

    print('{:,.5f}  | {:,.5f}   | {:,.5f}'.format(scores['KNN'], scores['log'], scores['svc']))


def standardize(X_train, X_test):
    X_train_std = SCALER.fit_transform(X_train)

    X_test_std = SCALER.transform(X_test)

    return X_train_std, X_test_std


def run_forest(X, y):
    spinner.start()

    forest.fit(X, y)

    spinner.stop()

    return True


def print_feature_importances():
    feature_importances_ = forest.feature_importances_

    sorted_features = np.argsort(feature_importances_)[::-1]

    print('')

    print('*Feature Importance*')

    print('')

    print('Rank      |    Feature     | Importance')

    print(':-------- | :------------- | ---------:')

    num = 0

    for i in sorted_features:
        num += 1
    print('{} | {:f}'.format(num, float(feature_importances_[i])))

    print('')
