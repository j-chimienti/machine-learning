import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { WineComponent } from './wine/wine.component';
import {CommonModule} from "@angular/common";


import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import {WineService} from "./wine.service";

@NgModule({
  declarations: [
    AppComponent,
    WineComponent,

  ],
  imports: [
    NgbModule.forRoot(),
    BrowserModule,
    CommonModule,
  ],
  providers: [
    WineService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
