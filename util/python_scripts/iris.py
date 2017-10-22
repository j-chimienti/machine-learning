
from sklearn import datasets

from classify import Classify

import pandas as pd


iris = datasets.load_iris()

X = iris.data

y = iris.target

columns = [
  'Sepal length', 'Sepal width', "Petal length", "Petal width"
]

Dataframe = pd.DataFrame(X)

Dataframe.columns = columns

X_ = Dataframe.iloc[::].values

classifier = Classify(X_, y, types = ['KNN', 'svc', 'log'])


