import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-boston-housing',
  templateUrl: './boston-housing.component.html',
  styleUrls: ['./boston-housing.component.css']
})
export class BostonHousingComponent implements OnInit {


  roomVPrice = {
    slope: 9.102,
    Intercept: -34.671
  }

  constructor() { }

  ngOnInit() {
  }

}
