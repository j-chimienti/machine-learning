import pandas as pd

from classify import Classify

url_base = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-{}.csv'


def classify_wine(wine='red'):
  url = url_base.format(wine)

  data = pd.read_csv(url, header=0, sep=';')

  X = data.iloc[:, :-1].values

  y = data.iloc[:, -1].values

  columns = [*data.columns]

  print('')
  print('# {} Wine Quality'.format(wine.capitalize()))

  print('')

  Classify(X, y, standardizeData=True, columns=columns)


classify_wine('red')

classify_wine('white')
