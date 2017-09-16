export class Wine {
  "fixed acidity": string;
  "volatile acidity": string;
  "citric acid": string;
  "residual sugar": string;
  "chlorides": string;
  "free sulfur dioxide": string;
  "total sulfur dioxide": string;
  "density": string;
  "pH": string;
  "sulphates": string;
  "alcohol": string;
  "quality": number;
  "test": boolean;
  prediction?: number = null;
  accuracy?: number = null;
}
