import { Component, Input, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProgressSpinnerModule } from 'primeng/progressspinner';
@Component({
  selector: 'app-display-results',
  imports: [CommonModule, ProgressSpinnerModule],
  templateUrl: './display-results.component.html',
  styleUrl: './display-results.component.scss'
})
export class DisplayResultsComponent {
  @Input() videoUrl: string | null = null;
  @Input() violations: number| null = 0;
  @Input() isLoading:boolean=false;
}