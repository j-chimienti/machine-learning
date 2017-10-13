const request = require('request-promise'), fs = require('fs'), csv = require('csv');
const assert = require("assert");

const columns = ["fixed acidity",
  "volatile acidity",
  "citric acid",
  "residual sugar",
  "chlorides",
  "free sulfur dioxide",
  "total sulfur dioxide",
  "density",
  "pH",
  "sulphates",
  "alcohol",
  "quality"];


const whiteWineUrl = {
  url: 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv',
  fileName: 'wine-quality-white.json',
  columns
};

const redWineUrl = {
  url: 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv',
  fileName: 'wine-quality-red.json',
  columns,
};

const wineClassify = {
  url: `http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data`,
  fileName: 'wineClassify.json',
  columns: ['Class label', 'Alcohol', 'Malic acid', 'Ash',
    'Alcalinity of ash', 'Magnesium', 'Total phenols',
    'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
    'Color intensity', 'Hue',
    'OD280/OD315 of diluted wines', 'Proline']
};




module.exports = function () {


  let wine = wineClassify;

  const w = process.argv[2];
  if (w === 'red') {

    wine = redWineUrl;
  } else if (w === 'white') {

    wine = whiteWineUrl;
  }

  assert(wine.url && wine.columns && wine.fileName);


  let delimiter = ',';


  if (wine === redWineUrl || wine === whiteWineUrl) {

    delimiter = ';';

  }

  const options_ = {delimiter, columns: wine.columns};

  request(wine.url).then(result => {


    csv.parse(result, options_, (err, result) => {

      if (err) throw err;

      fs.writeFile(wine.fileName, JSON.stringify(result, null, 4), () => {
        console.log('done');
      })

    })


  })


}();
