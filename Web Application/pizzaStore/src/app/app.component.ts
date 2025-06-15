import { Component } from '@angular/core';
import { UploadVideoComponent } from '../frontend/upload-video/upload-video.component';

@Component({
  selector: 'app-root',
  imports: [UploadVideoComponent],
  templateUrl: './app.component.html'
})
export class AppComponent {
  title = 'pizzaStore';
}
