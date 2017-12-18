from sklearn.ensemble import RandomForestClassifier

from sklearn import neighbors, linear_model, preprocessing, svm

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

SCALER = StandardScaler()

svc = svm.LinearSVC()

KNN = neighbors.KNeighborsClassifier()

logistic = linear_model.LogisticRegression(C=1e5)

forest = RandomForestClassifier(n_estimators=10000,
                                random_state=0,
                                n_jobs=-1)

types = ['KNN', 'svc', 'log']


def classify(X, y, standardize_data=False):
    x_train, x_test, y_train, y_test = split_test_data(X, y)

    if standardize_data:
        X_train_std, X_test_std = standardize(x_train, x_test)

        x_train = X_train_std

        x_test = X_test_std

    scores = {}

    predictions = {}

    for type_ in types:
        classifier = {'KNN': KNN, 'log': logistic, 'svc': svc}.get(type_, '')

        classifier.fit(x_train, y_train)

        predictions[type_] = classifier.predict(x_test)

        scores[type_] = classifier.score(x_test, y_test)

    forest.fit(x_train, y_train)

    return scores, predictions, forest.feature_importances_


def split_test_data(X, y):
    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size=0.3, random_state=0)

    return X_train, X_test, y_train, y_test


def standardize(X_train, X_test):
    X_train_std = SCALER.fit_transform(X_train)

    X_test_std = SCALER.transform(X_test)

    return X_train_std, X_test_std
