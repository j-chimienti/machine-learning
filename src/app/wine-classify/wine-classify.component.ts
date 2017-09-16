import {Component, Input, OnInit} from '@angular/core';
import {WineService} from "../wine.service";

@Component({
  selector: 'app-wine-classify',
  templateUrl: './wine-classify.component.html',
  styleUrls: ['./wine-classify.component.css']
})



export class WineClassifyComponent implements OnInit {


  @Input('wine') wine: string;

  public featureImportance: any[] = [];

  public testData: any[] = [];

  public trainData: any[] = [];

  public avg: number = 0;

  public url: string = null;

  public loading: boolean = false;


  constructor(private wineService: WineService) {
  }

  ngOnInit(): void {


    this.loading = true;


    this.setupData(this.wine);

    this.loading = false;

  }

  ngOnChanges(): void {

    this.loading = true;

    this.setupData(this.wine);

    this.loading = false;
  }

  private setupData(wine: string = 'classify'): void {


    this.wineService.getWineData(wine).then(data => {

      this.avg = data.avg;
      const {testData, trainData, url, featureImportance} = data;

      this.testData = testData;
      this.trainData = trainData;
      this.url = url;

      this.featureImportance = featureImportance;
    })


  }


}
