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


  public url: string = 'FIXME';

  public WINE : Wine;


  constructor(private wineService: WineService) {

    this.WINE = this.wineService.redWine;
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
