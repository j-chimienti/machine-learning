import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppComponent} from './app.component';
import {WineComponent} from './wine-quality/wine.component';
import {CommonModule} from "@angular/common";


import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import {WineService} from "./wine.service";
import {WineClassifyComponent} from './wine-classify/wine-classify.component';
import {ResultsComponent} from './wine-classify/results/results.component';
import {NavLinksComponent} from './nav-links/nav-links.component';
import {FeatureImportanceComponent} from './wine-classify/feature-importance/feature-importance.component';
import {WelcomeComponent} from './welcome/welcome.component';
import {IrisComponent} from './iris/iris.component';
import {RouterModule, Routes} from "@angular/router";


const appRoutes: Routes = [

  {path: 'classify', component: WineClassifyComponent},
  {path: 'quality/:color', component: WineComponent},
  {path: 'iris', component: IrisComponent},

  {path: '', component: WelcomeComponent}
];

@NgModule({
  declarations: [
    AppComponent,
    WineComponent,
    WineClassifyComponent,
    ResultsComponent,
    NavLinksComponent,
    FeatureImportanceComponent,
    WelcomeComponent,
    IrisComponent,
  ],
  imports: [


    RouterModule.forRoot(
      appRoutes,
      {enableTracing: false}
    ),
    NgbModule.forRoot(),
    BrowserModule,
    CommonModule
  ],
  providers: [
    WineService
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}
