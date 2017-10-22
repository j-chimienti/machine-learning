import pandas as pd

from classify import Classify

import sys

whiteWineUrl = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'

redWineUrl = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'

url = redWineUrl if len(sys.argv) == 2 and sys.argv[1] == 'red' else whiteWineUrl

wineQualityData = pd.read_csv(url, header=0, sep=';')

# print(wineQualityData.head())

X = wineQualityData.iloc[:, :-1].values

# get last col
y = wineQualityData.iloc[:, -1].values

print('')
print('# Wine Quality')

print('')

classifier_ = Classify(X, y, standardizeData=True)
