import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-feature-importance',
  templateUrl: './feature-importance.component.html',
  styleUrls: ['./feature-importance.component.css']
})
export class FeatureImportanceComponent implements OnInit {

  @Input('featureImportance') featureImportance: any;

  constructor() { }

  ngOnInit() {
  }

}
