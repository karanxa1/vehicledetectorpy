# 🚗 Vehicle Detection System using YOLOv5 & Streamlit

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Framework](https://img.shields.io/badge/Framework-Streamlit-red.svg)](https://streamlit.io)
[![Model](https://img.shields.io/badge/Model-YOLOv5-orange.svg)](https://github.com/ultralytics/yolov5)
[![License](https://img.shields.io/badge/License-Open%20Source-green.svg)]()
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://vehicledetector.streamlit.app/)

**Detect Cars, Trucks, Buses, Motorcycles, and Bicycles in your videos with ease!**

This project provides a user-friendly web application built with Streamlit to perform vehicle detection on uploaded videos using the powerful YOLOv5 object detection model.

---

## ✨ Live Demo

**Check out the hosted application:**
➡️ [**https://vehicledetector.streamlit.app/**](https://vehicledetector.streamlit.app/)

---

## 🎬 Showcase

*(Optional: Insert a GIF or screenshot of the app in action here!)*
`![Vehicle Detection Demo GIF](placeholder.gif)`

---

## 📌 Core Features

* **Multi-Class Detection:** Identifies `Cars`, `Trucks`, `Buses`, `Motorcycles`, and `Bicycles`.
* **State-of-the-Art Model:** Leverages `YOLOv5s` for efficient and accurate detection.
* **User-Friendly Interface:** Simple web app powered by `Streamlit` for easy video uploads and interaction.
* **Real-time Feedback:** Displays processing progress.
* **Visualize Results:** Play back the processed video with bounding boxes and labels directly in the app.
* **Download Output:** Option to download the processed video.
* **Wide Format Support:** Accepts `MP4`, `AVI`, `MOV`, `MKV` video files.

---

## 📂 Project Structure

/vehicle-detection-system│├── static/                # Stores uploaded & processed videos│   ├── uploaded_videos/   # Temporary storage for uploads│   └── processed_videos/  # Output storage for processed videos│├── streamlit_app.py       # Main Streamlit application script├── requirements.txt       # List of Python dependencies├── README.md              # This documentation file└── yolov5s.pt             # Pre-trained YOLOv5 model weights
---

## 🚀 Getting Started: Local Setup

Follow these steps to run the application locally:

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>  # Replace <repository-url> with your repo URL
cd vehicle-detection-system
2️⃣ Install DependenciesEnsure you have Python 3.8 or newer installed. Create a virtual environment (recommended) and install the required packages:python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
3️⃣ Download YOLOv5 Model (if needed)The yolov5s.pt file should be in your repository. If not, ensure it's placed in the root directory. YOLOv5 might download additional components on the first run.4️⃣ Run the Streamlit Appstreamlit run streamlit_app.py
Your default web browser should open automatically to the app. If not, navigate to:🔗 http://localhost:8501/☁️ Deploying to Streamlit CloudShare your app with the world!1️⃣ Prepare Your GitHub RepositoryPush your project code to a GitHub repository.Ensure the repository contains:streamlit_app.pyrequirements.txtyolov5s.pt (ensure Git LFS is configured if the file is large)The static/ folder structure (even if empty initially, or use code to create it).2️⃣ Deploy via Streamlit CloudVisit Streamlit Cloud and sign in with GitHub.Click "New app" and select "Deploy from existing repo".Choose your repository, branch (main or master), and set the Main file path to streamlit_app.py.Click "Deploy!".Note: For handling larger video files or models, you might need to select a paid resource tier or adjust memory in the app's advanced settings on Streamlit Cloud.📖 How to Use the AppUpload: Use the file uploader in the web interface to select a video file (MP4, AVI, MOV, MKV).Process: Click the "Process Video" button.Wait: Monitor the progress bar as the system analyzes the video frame by frame.View: Once completed, the processed video will appear in the app, showing detected vehicles with bounding boxes.Download: Use the "Download Processed Video" button to save the result.⚙️ Video Processing InsightsObject detection is performed using the yolov5s.pt model weights.Detected vehicles are marked with green bounding boxes.A running count of detected vehicles might be displayed (based on your streamlit_app.py logic).Processed videos are temporarily stored on the server in the static/processed_videos/ directory before being offered for download.🛠️ Troubleshooting TipsModel Loading Failed:Verify yolov5s.pt is present in the project's root directory.Check internet connection (for first-time component downloads by YOLO).Video Processing Errors:Confirm the uploaded video format is supported.Try smaller or shorter video files (large files need more RAM/processing time).Ensure sufficient disk space if running locally.Streamlit App Issues:Confirm Python version is 3.8+.Re-check dependencies: pip install -r requirements.txt.Look for specific error messages in the terminal where you ran streamlit run.
