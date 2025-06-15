import { Component, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DisplayResultsComponent } from "../display-results/display-results.component";
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-upload-video',
  imports: [CommonModule, DisplayResultsComponent],
  templateUrl: './upload-video.component.html',
  styleUrl: './upload-video.component.scss'
})
export class UploadVideoComponent {
  videoUrl = signal<string | null>(null);
  violations = signal<number | null>(null);
  fileName: string = '';
  isLoading = signal(false);
  private http = inject(HttpClient);

  handleFile(event: Event) {
    const input = event.target as HTMLInputElement;
    const file = input.files?.[0];
    if (!file) return;
    this.isLoading.set(true);
    this.fileName = file.name;
    const formData = new FormData();
    formData.append('video', file);

    this.http.post<{ processedVideoUrl: string; detectionCount: number }>('http://localhost:8080/process-video', formData)
    .subscribe(response => 
      {
        this.videoUrl.set(response.processedVideoUrl);
        this.violations.set(response.detectionCount);
        this.isLoading.set(false);
      }
    );
  }
}
