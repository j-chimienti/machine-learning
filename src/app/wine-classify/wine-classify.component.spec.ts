import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WineClassifyComponent } from './wine-classify.component';

describe('WineClassifyComponent', () => {
  let component: WineClassifyComponent;
  let fixture: ComponentFixture<WineClassifyComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WineClassifyComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WineClassifyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
