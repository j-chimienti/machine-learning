import pandas as pd

from classify import Classify

df_wine = pd.read_csv('https://archive.ics.uci.edu/'
                      'ml/machine-learning-databases/wine/wine.data',
                      header=None)

columns = ['Class label', 'Alcohol', 'Malic acid', 'Ash',
                   'Alcalinity of ash', 'Magnesium', 'Total phenols',
                   'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
                   'Color intensity', 'Hue', 'OD280/OD315 of diluted wines',
                   'Proline']

df_wine.columns = columns

X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values


print('')
print('# Wine Classify')

print('')

classifier = Classify(X, y, columns = columns, standardizeData =  True)

