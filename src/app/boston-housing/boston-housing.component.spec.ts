import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BostonHousingComponent } from './boston-housing.component';

describe('BostonHousingComponent', () => {
  let component: BostonHousingComponent;
  let fixture: ComponentFixture<BostonHousingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BostonHousingComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BostonHousingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
