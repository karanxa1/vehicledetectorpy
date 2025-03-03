import torch
import cv2
import numpy as np

# Load YOLOv5 model
model = torch.hub.load("ultralytics/yolov5", "custom", path="yolov5s.pt", force_reload=True)

# Class labels for vehicle detection (adjust as per YOLOv5 model)
VEHICLE_CLASSES = {"car", "truck", "bus", "motorcycle", "bicycle"}

def detect_vehicles(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, 30, (int(cap.get(3)), int(cap.get(4))))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        detections = results.pandas().xyxy[0]
        
        vehicle_count = {"car": 0, "truck": 0, "bus": 0, "motorcycle": 0, "bicycle": 0}

        for _, row in detections.iterrows():
            label = row["name"]
            if label in VEHICLE_CLASSES:
                vehicle_count[label] += 1
                x1, y1, x2, y2 = int(row["xmin"]), int(row["ymin"]), int(row["xmax"]), int(row["ymax"])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        count_text = " | ".join([f"{k}: {v}" for k, v in vehicle_count.items()])
        cv2.putText(frame, count_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        out.write(frame)

    cap.release()
    out.release()