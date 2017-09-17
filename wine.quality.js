const request = require('request-promise'), fs = require('fs'), csv = require('csv');


const whiteWineUrl = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality-quality/winequality-white.csv';

const redWineUrl = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality-quality/winequality-red.csv';


const wineClassify = 'https://archive.ics.uci.edu/ml/' +
  'machine-learning-databases/wine-quality/wine-quality.data';

module.exports = function () {


  request(wineClassify).then(result => {


    csv.parse(result, {delimiter: ",", columns: ['Class label', 'Alcohol', 'Malic acid', 'Ash',
      'Alcalinity of ash', 'Magnesium', 'Total phenols',
      'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
      'Color intensity', 'Hue',
      'OD280/OD315 of diluted wines', 'Proline']}, (err, result) => {

      if (err) throw err;

      fs.writeFile('wine.classify.json', JSON.stringify(result, null, 4), () => {
        console.log('done');
      })

    })


  })


}();
