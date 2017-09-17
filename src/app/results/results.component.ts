import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.css']
})
export class ResultsComponent implements OnInit {


  @Input('accuracy') accuracy: {test: number, training: number};



  constructor() { }

  ngOnInit() {
  }

}
