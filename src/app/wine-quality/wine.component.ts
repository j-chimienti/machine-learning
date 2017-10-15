import {Component, Input, OnDestroy, OnInit} from '@angular/core';
import {Wine} from "./WINE";

import {WineService} from "../wine.service";
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'app-wine',
  templateUrl: './wine.component.html',
  styleUrls: ['./wine.component.css']
})
export class WineComponent implements OnInit {


  public WINE: any;

  public color: string;


  constructor(private wineService: WineService, private router: Router, private route: ActivatedRoute) {
  }

  ngOnInit(): void {


    this.color = this.route.snapshot.params['color'];

    this.WINE = this.wineService.getWineQuality(this.color);


  }

}
