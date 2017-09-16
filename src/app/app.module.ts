import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { WineComponent } from './wine/wine.component';
import {CommonModule} from "@angular/common";


import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import {WineService} from "./wine.service";
import { WineClassifyComponent } from './wine-classify/wine-classify.component';

@NgModule({
  declarations: [
    AppComponent,
    WineComponent,
    WineClassifyComponent,

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
