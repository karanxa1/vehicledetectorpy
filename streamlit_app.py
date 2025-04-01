import streamlit as st
import torch
import cv2
import numpy as np
import os
import uuid
import tempfile
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="Vehicle Detection System",
    page_icon="🚗",
    layout="wide"
)

# Get the absolute path of the current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define folders with absolute paths
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static/uploaded_videos")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "static/processed_videos")
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv'}

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load YOLOv5 model
@st.cache_resource
def load_model():
    model_path = os.path.join(BASE_DIR, "vehicle dtectorpy/yolov5s.pt")
    model = torch.hub.load("ultralytics/yolov5", "custom", path=model_path, force_reload=True)
    return model

# Class labels for vehicle detection
VEHICLE_CLASSES = {"car", "truck", "bus", "motorcycle", "bicycle"}

def detect_vehicles(video_path, output_path, progress_bar):
    model = load_model()
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    # Get total frame count for progress bar
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        # Update progress bar
        frame_count += 1
        progress_bar.progress(frame_count / total_frames)
        
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
    return output_path

# Main app
def main():
    st.title("🚗 Vehicle Detection System")
    st.markdown("""
    Upload a video to detect and count vehicles. The system detects cars, trucks, buses, motorcycles, and bicycles.
    
    Supported formats: MP4, AVI, MOV, MKV
    """)
    
    # File uploader
    uploaded_file = st.file_uploader("Choose a video file", type=list(ALLOWED_EXTENSIONS))
    
    if uploaded_file is not None:
        # Display file info
        file_details = {
            "Filename": uploaded_file.name,
            "File size": f"{uploaded_file.size / (1024*1024):.2f} MB"
        }
        st.write(file_details)
        
        # Save uploaded file to temp location
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())
        video_path = tfile.name
        
        # Create unique output filename
        unique_filename = f"{uuid.uuid4()}_{uploaded_file.name}"
        output_filename = f"processed_{unique_filename}"
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)
        
        # Process button
        if st.button("Process Video"):
            with st.spinner("Processing video..."):
                # Create a progress bar
                progress_bar = st.progress(0)
                
                # Process the video
                try:
                    detect_vehicles(video_path, output_path, progress_bar)
                    st.success("Video processed successfully!")
                    
                    # Display the processed video
                    st.subheader("Processed Video with Detections")
                    st.video(output_path)
                    
                    # Provide download link
                    with open(output_path, "rb") as file:
                        st.download_button(
                            label="Download Processed Video",
                            data=file,
                            file_name=output_filename,
                            mime="video/mp4"
                        )
                except Exception as e:
                    st.error(f"Error processing video: {str(e)}")
                finally:
                    # Clean up the temporary file
                    os.unlink(video_path)

if __name__ == "__main__":
    main()