import {Component, Input, OnInit} from '@angular/core';
import {WineService} from "../wine.service";
import {Wine} from "../wine-quality/WINE";

@Component({
  selector: 'app-wine-classify',
  templateUrl: './wine-classify.component.html',
  styleUrls: ['./wine-classify.component.css']
})


export class WineClassifyComponent implements OnInit {


  @Input('wine') wine: string;

  public featureImportance: any[] = [];

  public url: string = 'FIXME';

  public loading: boolean = false;

  public WINE : Wine;


  constructor(private wineService: WineService) {

    this.WINE = this.wineService.redWine;
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


    this.WINE = this.wineService.getWineQuality(wine);

    this.featureImportance = this.WINE.featureImportance;

  }


}
