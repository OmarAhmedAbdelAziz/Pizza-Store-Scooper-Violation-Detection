# 🍕 Pizza Store Scooper Violation Detection

This project detects hygiene violations in a pizza store by identifying when workers use their hands inside food containers instead of scoopers. It uses object detection with YOLOv8-nano and is deployed as a web-based system with microservices architecture.

---

## 🚀 Features

- Detects persons, containers, and scoopers using YOLOv8-nano
- Flags violations when hands enter containers without scoopers
- Manually defined ROIs for container zones
- Microservices architecture:
  - Flask backend for video processing
  - Angular frontend for uploading videos and viewing results

---

## 🧠 Model

- **Model:** YOLOv8-nano (`yolov8n.pt`)
- **Trained On:** Custom dataset via Roboflow
- **Classes:** `person`, `scooper`, `container`

---

## 🛠️ Tech Stack

- YOLOv8 (Ultralytics)
- Python, OpenCV
- Flask (backend API)
- Angular (frontend UI)
- Roboflow (dataset management)
