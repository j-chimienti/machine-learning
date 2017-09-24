import {Component, Input, OnInit} from '@angular/core';
import {WineService} from "../wine.service";

@Component({
  selector: 'app-wine-classify',
  templateUrl: './wine-classify.component.html',
  styleUrls: ['./wine-classify.component.css']
})


export class WineClassifyComponent implements OnInit {


  @Input('wine') wine: string;


  public WINE : any;


  constructor(private wineService: WineService) {

    this.WINE = this.wineService.classifiedWine;
  }

  ngOnInit(): void {



    this.setupData(this.wine);

  }

  ngOnChanges(): void {

    this.setupData(this.wine);
  }

  private setupData(wine: string = 'classify'): void {


    this.WINE = this.wineService.getWineQuality(wine);


  }


}
