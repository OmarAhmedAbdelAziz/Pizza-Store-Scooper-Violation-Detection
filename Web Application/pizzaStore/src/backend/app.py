from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import uuid
import shutil
from violation_detector import run_model

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

VIDEO_DIR = 'videos'
os.makedirs(VIDEO_DIR, exist_ok=True)

@app.route('/process-video', methods=['POST']) #creates API
def process_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video uploaded'}), 400

    video_file = request.files['video']
    video_id = str(uuid.uuid4())
    input_path = os.path.join(VIDEO_DIR, f"input_{video_id}.mp4")
    video_file.save(input_path)
    output_filename, count = run_model(input_path)
    return jsonify({
        "processedVideoUrl": f"http://localhost:8080/videos/{output_filename}",
        "detectionCount": count
    })

@app.route('/videos/<filename>')
def serve_video(filename):
    return send_from_directory(VIDEO_DIR, filename, mimetype='video/mp4')

if __name__ == "__main__":
    app.run(debug=True, port=8080)