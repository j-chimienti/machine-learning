import {Injectable} from '@angular/core';


const whiteWine = {
  accuracy: {
    test: 0.5,
    training: 0.5
  },
  featureImportance: [

  ],

};


const redWine = {

  accuracy: {
    test: 0.5,
    training: 0.5
  },
  featureImportance: [

  ],

}


const classifiedWine = {

  accuracy: {
    test: 0.851851851852,
    training: 0.862903225806,
  },
  hello:
    ` 1) Proanthocyanins                0.182483
 2) OD280/OD315 of diluted wines   0.158610
 3) Total phenols                  0.150948
 4) Hue                            0.131987
 5) Class label                    0.106589
 6) Color intensity                0.078243
 7) Magnesium                      0.060718
 8) Ash                            0.032033
 9) Alcohol                        0.025400
10) Nonflavanoid phenols           0.022351
11) Alcalinity of ash              0.022078
12) Flavanoids                     0.014645
13) Malic acid                     0.013916`
  ,
  goodImportance: ` 1) Color intensity                0.182483
 2) Proline                        0.158610
 3) Flavanoids                     0.150948
 4) OD280/OD315 of diluted wines   0.131987
 5) Alcohol                        0.106589
 6) Hue                            0.078243
 7) Total phenols                  0.060718
 8) Alcalinity of ash              0.032033
 9) Malic acid                     0.025400
10) Proanthocyanins                0.022351
11) Magnesium                      0.022078
12) Nonflavanoid phenols           0.014645
13) Ash                            0.013916`,
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


  public getWineQuality(wine: string = 'white'): any {


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
