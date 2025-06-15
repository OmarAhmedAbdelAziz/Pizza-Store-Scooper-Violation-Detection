import { Component } from '@angular/core';
import { UploadVideoComponent } from '../frontend/upload-video/upload-video.component';

@Component({
  selector: 'app-root',
  imports: [UploadVideoComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'pizzaStore';
}
