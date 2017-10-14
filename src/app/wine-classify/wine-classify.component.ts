import {Component, Input, OnInit} from '@angular/core';
import {WineService} from "../wine.service";

@Component({
  selector: 'app-wine-classify',
  templateUrl: './wine-classify.component.html',
  styleUrls: ['./wine-classify.component.css']
})


export class WineClassifyComponent implements OnInit{


  public WINE: any = null;


  constructor(private wineService: WineService) {


  }

  ngOnInit() {

    this.WINE = this.wineService.classifiedWine;
  }



}
