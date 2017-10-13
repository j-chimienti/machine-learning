import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FeatureImportanceComponent } from './feature-importance.component';

describe('FeatureImportanceComponent', () => {
  let component: FeatureImportanceComponent;
  let fixture: ComponentFixture<FeatureImportanceComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FeatureImportanceComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FeatureImportanceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
