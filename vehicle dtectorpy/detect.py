import os
import cv2
import torch

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5s.pt', force_reload=True)
model.conf = 0.3  # Lowered confidence threshold for detecting smaller vehicles

# List of vehicle classes to detect (Check YOLO class names!)
VEHICLE_CLASSES = ["car", "truck", "tuktuk", "bus", "van", "jeep", "motorcycle"]  # "motorcycle" includes bikes & scooters

def detect_vehicles(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    fourcc = cv2.VideoWriter_fourcc(*'avc1')  # H.264 codec
    fps = int(cap.get(cv2.CAP_PROP_FPS)) if cap.get(cv2.CAP_PROP_FPS) > 0 else 30
    frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    out = cv2.VideoWriter(output_path, fourcc, fps, frame_size)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        for *box, conf, cls in results.xyxy[0]:  # Bounding box, confidence, class
            label = model.names[int(cls)]

            if label in VEHICLE_CLASSES:
                color = (0, 255, 0)  # Green bounding box
                cv2.rectangle(frame, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), color, 2)
                cv2.putText(frame, f"{label} ({conf:.2f})", (int(box[0]), int(box[1]) - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        out.write(frame)

    cap.release()
    out.release()
