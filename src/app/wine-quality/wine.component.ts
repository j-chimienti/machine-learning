import {Component, Input, OnInit} from '@angular/core';
import {Wine} from "./WINE";

import {WineService} from "../wine.service";


@Component({
  selector: 'app-wine',
  templateUrl: './wine.component.html',
  styleUrls: ['./wine.component.css']
})
export class WineComponent implements OnInit {


  @Input('wine') wine: string;

  public featureImportance: any[] = [];


  public url: string = 'FIXME';

  public loading: boolean = false;

  public WINE : Wine = null;


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

  private setupData(wine: string = 'white'): void {


    this.WINE = this.wineService.getWineQuality(wine);

    this.featureImportance = this.WINE.featureImportance;


  }


}
