🚗 Vehicle Detection System
A robust AI-powered video analytics solution
Show Image
This Streamlit web application detects and classifies vehicles (cars, trucks, buses, motorcycles, bicycles) from uploaded videos using YOLOv5, providing real-time analytics and visualization.
➡️ Try it now: vehicledetector.streamlit.app

✨ Key Features

🔍 Multi-vehicle detection: Accurately identifies cars, trucks, buses, motorcycles, and bicycles
🧠 Powered by YOLOv5: State-of-the-art object detection model for high accuracy
📊 Real-time analytics: Track processing progress with a live status bar
🎬 Instant visualization: Watch processed videos with highlighted vehicle detections
💾 Easy export: Download processed videos with a single click
📁 Broad compatibility: Supports MP4, AVI, MOV, MKV video formats
☁️ Cloud-ready: Optimized for Streamlit Cloud deployment


📂 Project Structure
/vehicle-detection-system
│
├── /static                  # Media storage directory
│   ├── /uploaded_videos     # Temporary storage for user uploads
│   └── /processed_videos    # Output directory for analyzed videos
│
├── streamlit_app.py         # Main application logic
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation
└── yolov5s.pt               # Pre-trained YOLOv5 model weights

🚀 Installation & Setup
Local Development
bash# Clone the repository
git clone <repository-url>
cd vehicle-detection-system

# Install dependencies (Python 3.8+ required)
pip install -r requirements.txt

# Launch the application
streamlit run streamlit_app.py
Your browser will open automatically to http://localhost:8501
Cloud Deployment

Fork/Push to GitHub

Ensure all required files are included
Maintain the proper directory structure


Deploy on Streamlit Cloud

Visit Streamlit Cloud
Connect your GitHub account
Select your repository
Set main file to streamlit_app.py
Click "Deploy"


Optimize Performance (Optional)

Adjust memory allocation for larger videos
Configure theme and appearance settings




📱 How to Use

Upload your video through the intuitive drag-and-drop interface
Process with a single click
Watch as AI detects and labels each vehicle in real-time
Analyze the results with color-coded bounding boxes
Download the processed video for sharing or further analysis


🔧 Technical Details

Detection Engine: YOLOv5 (You Only Look Once) neural network
Visualization: Green bounding boxes with class labels
Performance: Optimized for real-time processing
Analytics: Vehicle count and classification statistics


⚠️ Troubleshooting
Common Issues & Solutions
ProblemSolutionModel Loading FailsVerify yolov5s.pt exists in root directoryProcessing ErrorsTry smaller videos or check supported formatsMemory IssuesIncrease available RAM or reduce video resolutionMissing DependenciesRun pip install -r requirements.txtStreamlit Connection IssuesCheck your internet connection and firewall settings

👨‍💻 Developer
Developed with ❤️ by Karan Rajput
📧 Contact: karanravirajput@gmail.com

📄 License
This project is open-source and free to use.
Contributions and improvements are welcome! Fork, modify, and submit pull requests to help enhance this tool.

🔗 Live Demo: vehicledetector.streamlit.app
