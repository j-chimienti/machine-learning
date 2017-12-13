from sklearn import datasets

from analysis import classify

import pandas as pd

import numpy as np

iris = datasets.load_iris()

X = iris.data

y = iris.target

columns = [
    'Sepal length', 'Sepal width', "Petal length", "Petal width"
]

Dataframe = pd.DataFrame(X)

Dataframe.columns = columns

X_ = Dataframe.iloc[::].values

print('')

print('# Iris')

print('')

classify(X_, y, standardize_data=False, columns=columns)
