const request = require('request-promise'), fs = require('fs'), csv = require('csv');


const whiteWineUrl = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv';

const redWineUrl = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv';

module.exports = function () {


  request(redWineUrl).then(result => {


    csv.parse(result, {delimiter: ";", columns: true}, (err, result) => {

      if (err) throw err;

      fs.writeFile('wine.red.quality.json', JSON.stringify(result, null, 4), () => {
        console.log('done');
      })

    })


  })


}();
