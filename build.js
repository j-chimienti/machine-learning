const marked = require('marked');

const fs = require('fs');


const navLinks = `<div>
  <ul>
    <li>

      <a  class="text-capitalize" href="#summary">summary</a>
    </li>
    <li><a  class="text-capitalize"  href="#results">results</a></li>
    <li><a  class="text-capitalize"  href="#featureImportance">feature Importance</a></li>
    <li><a  class="text-capitalize"  href="#references">references</a></li>
  </ul>
</div>`;

const iris = {
  references: ` <section id="references">
    <h3>References</h3>
    <ul>
      <li>Source: <a
        href="https://archive.ics.uci.edu/ml/datasets/Iris">https://archive.ics.uci.edu/ml/datasets/Iris</a>
      </li>
      <li>Bache, K. &amp; Lichman, M. (2013). UCI Machine Learning Repository. Irvine, CA: University of California,
        School of Information and Computer Science.
      </li>
    </ul>
  </section>
`,

  classNames: {
    0: 'Iris-setosa',
    1: 'Iris-versicolor',
    2: 'Iris-virginica',
  },
  summary: ` <section id="summary">
    <h2>Iris flower dataset</h2>
    <p>
      Fisher’s Iris data base (Fisher, 1936) is perhaps the best known
      database to be found in the pattern recognition literature. The data
      set contains 3 classes of 50 instances each, where each class refers
      to a type of iris plant. One class is linearly separable from the other
      two; the latter are not linearly separable from each other.
    </p>


    <p><strong>Features</strong></p>
    <ol>
      <li>Sepal length</li>
      <li>Sepal width</li>
      <li>Petal length</li>
      <li>
        <p>Petal width</p>
      </li>
      <li>
        <p>Number of samples: 150</p>
      </li>
      <li>
        <p>Target variable (discrete): 50x Setosa, 50x Versicolor, 50x Virginica</p>
      </li>
    </ol>

  </section>`,

  results: marked(
    `
    ### Results

KNN | Logistic Regression | Linear SVC
--- | ------------------- | --------- |
 0.977778 | 0.977778 | 0.933333

*Feature Importance*

num | Feature | Importance
--- | -------- | ---------
1 | Petal length | 0.458107
2 | Petal width | 0.408683
3 | Sepal length | 0.107372
4 | Sepal width | 0.025838

    `
  ),


};


const wineClassify = {
  summary: `

  <h3 id="summary">Summary</h3>
  <p>
    These data are the results of a chemical analysis of wines grown in the same region in Italy but derived from
    three different cultivars. The analysis determined the quantities of 13 constituents found in each of the three
    types of wines.

  </p>
  <p>
    In a classification context, this is a well posed problem with "well behaved" class structures. A good data set
    for first testing of a new classifier, but not very challenging.


  </p>

`,
  references: `<section>
    <h3><a href="#references" id="references">References</a></h3>
    <ul>
      <li>Forina, M. et al, PARVUS -
        An Extendible Package for Data Exploration, Classification and Correlation.
        Institute of Pharmaceutical and Food Analysis and Technologies, Via Brigata Salerno,
        16147 Genoa, Italy.
      </li>
      <li>Source: <a
        href="https://archive.ics.uci.edu/ml/datasets/Wine">https://archive.ics.uci.edu/ml/datasets/Wine</a>
      </li>
      <li>Bache, K. &amp; Lichman, M. (2013). UCI Machine Learning Repository. Irvine, CA: University of California,
        School of Information and Computer Science.
      </li>
    </ul>

  </section>`,
  results: marked(
`
### Results

KNN | Logistic Regression | Linear SVC
--- | ------------------- | --------- |
 1.000000 | 1.000000 | 1.000000

*Feature Importance*

num | Feature | Importance
--- | -------- | ---------
1 | Proanthocyanins | 0.182483
2 | OD280/OD315 of diluted wines | 0.158610
3 | Total phenols | 0.150948
4 | Hue | 0.131987
5 | Class label | 0.106589
6 | Color intensity | 0.078243
7 | Magnesium | 0.060718
8 | Ash | 0.032033
9 | Alcohol | 0.025400
10 | Nonflavanoid phenols | 0.022351
11 | Alcalinity of ash | 0.022078
12 | Flavanoids | 0.014645
13 | Malic acid | 0.013916

`
  ),
  images: `
   <div class="text-center">
    <img src="./assets/images/alcohol.png" class="img-fluid rounded img-thumbnail"/>
  </div>

  <div class="text-center">
    <img src="./assets/images/colorIntensity.png" class="img-fluid rounded img-thumbnail"/>
  </div>

  <div class="text-center">
    <img src="./assets/images/flavonoids.png" class="img-fluid rounded img-thumbnail"/>
  </div>

  <div class="text-center">
    <img src="./assets/images/proline.png" class="img-fluid rounded img-thumbnail"/>
  </div>`,
}

const summary = marked(`
  
    ### Summary
    
    *fixme*
  `);

const references = marked(
  `
    ### References
  `
);

const wineQuality = {
  summary,
  red: {
    summary,
    results: marked(`
      

### Results

KNN | Logistic Regression | Linear SVC
--- | ------------------- | --------- |
 0.558333 | 0.627083 | 0.614583

*Feature Importance*

num | Feature | Importance
--- | -------- | ---------
1 | alcohol | 0.139313
2 | sulphates | 0.115662
3 | volatile acidity | 0.108089
4 | total sulfur dioxide | 0.102579
5 | density | 0.087899
6 | chlorides | 0.078694
7 | pH | 0.077515
8 | fixed acidity | 0.075735
9 | citric acid | 0.075266
10 | residual sugar | 0.071744
11 | free sulfur dioxide | 0.067503


    `),
    references,
  },
  white: {
    summary,
    results: marked(
`

### Results

KNN | Logistic Regression | Linear SVC
--- | ------------------- | --------- |
 0.544218 | 0.522449 | 0.519048

*Feature Importance*

num | Feature | Importance
--- | -------- | ---------
1 | alcohol | 0.115958
2 | density | 0.103242
3 | volatile acidity | 0.100965
4 | free sulfur dioxide | 0.096563
5 | total sulfur dioxide | 0.090816
6 | residual sugar | 0.086444
7 | chlorides | 0.085341
8 | pH | 0.084654
9 | citric acid | 0.081165
10 | sulphates | 0.080709
11 | fixed acidity | 0.074144


`
    ),
    references,
  }
}


const html = (...body) => `
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Machine Learning</title>
  <base href="/">



  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/x-icon" href="favicon.ico">

  <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Catamaran:100,200,300,400,500,600,700,800,900" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Muli" rel="stylesheet">


  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css"
        integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">

  <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
  <style>
    html,
    body {
      width: 100%;
      height: 100%;
    }

    body {
      font-family: 'Muli', 'Helvetica', 'Arial', 'sans-serif';
    }

    section {
      min-height: 80vh;
    }

    .table-fixed {
      max-height: 400px;
      overflow-y: scroll;
    }

  </style>


</head>
<body>

${body}

<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-108469762-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-108469762-1');
</script>



</body>
</html>

`

const irisBod = [navLinks, iris.summary, iris.results, iris.references];
const wineClassifyBody = [navLinks, wineClassify.summary, wineClassify.results, wineClassify.images, wineClassify.references];

const wineQualityRedBod = [navLinks, wineQuality.red.summary, wineQuality.red.results, wineQuality.red.references];
const wineQualityWhiteBod = [navLinks, wineQuality.white.summary, wineQuality.white.results, wineQuality.white.references];

return Promise.all([
  fs.writeFile('./iris.html', html(irisBod), () => {}),
  fs.writeFile('./wine-classify.html', html(wineClassifyBody), () => {}),
  fs.writeFile('./wine-quality-red.html', html(wineQualityRedBod), () => {}),
  fs.writeFile('./wine-quality-white.html', html(wineQualityWhiteBod), () => {}),

]).then(() => console.log('done'))
  .catch(console.error)


