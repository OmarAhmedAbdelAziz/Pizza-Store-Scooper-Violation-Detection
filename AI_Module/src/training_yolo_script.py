import gdown
import os
import cv2
from pathlib import Path
from ultralytics import YOLO
from roboflow import Roboflow


rf = Roboflow(api_key="R74jhKNUxfJpMqRD85bY")
project = rf.workspace("pizza-use-case").project("pizzastore")
version = project.version(4)
dataset = version.download("yolov8")

model = YOLO('yolov8n.pt')

model.train(
    data='/content/PizzaStore-4/data.yaml',
    epochs=100,
    imgsz=640,
    batch=16,
    device=0  
)
results = model.predict(source='/content/downloaded_videos/saah.mp4', save=True)
