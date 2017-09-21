import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { WineComponent } from './wine-quality/wine.component';
import {CommonModule} from "@angular/common";


import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import {WineService} from "./wine.service";
import { WineClassifyComponent } from './wine-classify/wine-classify.component';
import { SummaryComponent } from './summary/summary.component';
import { ResultsComponent } from './results/results.component';
import { NavLinksComponent } from './nav-links/nav-links.component';
import { FeatureImportanceComponent } from './feature-importance/feature-importance.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { IrisComponent } from './iris/iris.component';
import { BostonHousingComponent } from './boston-housing/boston-housing.component';

@NgModule({
  declarations: [
    AppComponent,
    WineComponent,
    WineClassifyComponent,
    SummaryComponent,
    ResultsComponent,
    NavLinksComponent,
    FeatureImportanceComponent,
    WelcomeComponent,
    IrisComponent,
    BostonHousingComponent,

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
