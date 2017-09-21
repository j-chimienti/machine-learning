import {Injectable} from '@angular/core';


interface WINE {
  accuracy: {
    test: number,
    training: number,
  },
  featureImportance: any[]
}

const whiteWine: WINE = {
  accuracy: {
    test: 0.521088435374,
    training: 0.541423570595,
  },
  featureImportance: [
    ['alcohol     ', 0.115958],
    ['density', 0.103242],
    ['volatile acidity    ', 0.100965],
    ['free sulfur dioxide ', 0.096563],
    ['total sulfur dioxide', 0.090816],
    ['residual sugar ', 0.086444],
    ['chlorides   ', 0.085341],
    ['pH  ', 0.084654],
    ['citric acid    ', 0.081165],
    ['sulphates ', 0.080709],
    ['fixed acidity  ', 0.074144],
  ],

};


const redWine: WINE = {

  accuracy: {
    test: 0.622916666667,
    training: 0.572832886506,
  },
  featureImportance: [
    [' alcohol        ', 0.139313],
    [' sulphates ', 0.115662],
    [' volatile acidity    ', 0.108089],
    [' total sulfur dioxide', 0.102579],
    [' density   ', 0.087899],
    [' chlorides ', 0.078694],
    [' pH   ', 0.077515],
    [' fixed acidity  ', 0.075735],
    [' citric acid    ', 0.075266],
    [' residual sugar ', 0.071744],
  ],

};


const classifiedWine : WINE = {

  accuracy: {
    test: 0.851851851852,
    training: 0.862903225806,
  },
  featureImportance: [
    ["Color intensity", 0.182483],
    ["Proline", 0.158610],
    ["Flavanoids", 0.150948],
    ["OD280/OD315 of diluted wines", 0.131987],
    ["Alcohol", 0.106589],
    ["Hue", 0.078243],
    ["Total phenols", 0.060718],
    ["Alcalinity of ash", 0.032033],
    ["Malic acid", 0.025400],
    ["Proanthocyanins", 0.022351],
    ["Magnesium", 0.022078],
    ["Nonflavanoid phenols", 0.014645],
    ["Ash", 0.013916],
  ],
}


@Injectable()
export class WineService {

  public redWine = redWine;

  constructor() {
  }


  public getWineQuality(wine: string = 'white'): WINE {


    let WINE;

    if (wine === 'white') {

      WINE = whiteWine;
    } else if (wine === 'red') {

      WINE = redWine;
    } else if (wine === 'classify') {

      WINE = classifiedWine;
    }


    return WINE;


  }


}
