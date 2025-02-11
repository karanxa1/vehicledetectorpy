# 🚗 Vehicle Detection Flask App

This project is a **Flask-based web application** that detects and classifies **vehicles** (Car, Truck, Tuk-Tuk, Bus, Bike, Scooter, etc.) from uploaded videos using **YOLOv5**.

---

## 📌 Features
👉 Detects multiple vehicle types: **Car, Truck, Tuk-Tuk, Bus, Bike, Scooter, etc.**  
👉 Uses **YOLOv5** for object detection  
👉 **Flask web app** for easy video uploading & processing  
👉 **Processed video playback** with detected vehicles  
👉 Supports **MP4, AVI, MOV, MKV** video formats  
👉 Uses **H.264 (`avc1`) encoding** for browser compatibility  

---

## 📂 Folder Structure
```
/vehicle-detection-app
│── /static                # Folder for storing uploaded & processed videos
│── /templates             # HTML files for Flask web interface
│── app.py                 # Flask web app
│── detect.py              # YOLOv5-based vehicle detection script
│── upload.html            # Frontend for video upload & playback
│── yolov5s.pt             # YOLOv5 model weights
│── README.md              # Project documentation
```

---

## 🚀 Installation & Setup

### **1⃣ Install Dependencies**
Make sure you have **Python 3.8+** installed. Then, run:

```bash
pip install flask flask-cors opencv-python torch torchvision
```

---

### **2⃣ Download YOLOv5**
The script automatically downloads YOLOv5 when you first run `app.py`. If you want to manually install it:

```bash
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```

---

### **3⃣ Run the Flask App**
```bash
python app.py
```
After running the command, open your browser and go to:  
🔗 **http://127.0.0.1:5000/**  

---

## 📅 How to Use
1. **Upload a video** via the web interface.  
2. The system will **process the video** and detect vehicles.  
3. Once complete, the **processed video will be displayed** with labeled vehicles.  

---

## 🎥 Video Processing Details
- Uses **YOLOv5 for vehicle detection**  
- Saves processed videos in **static/** directory  
- **Green bounding boxes** are drawn around detected vehicles  
- Uses **H.264 (`avc1`) encoding** for better browser support  

---

## 🛠️ Troubleshooting

### **1⃣ Model Not Detecting Two-Wheelers?**
- YOLOv5 may classify bikes & scooters as `"motorcycle"`.  
- Try **printing the model's class labels**:
  ```python
  import torch
  model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5s.pt')
  print(model.names)
  ```
  If `"motorcycle"` is listed, update `detect.py`:
  ```python
  VEHICLE_CLASSES = ["car", "truck", "tuktuk", "bus", "van", "jeep", "motorcycle"]
  ```
  - `"motorcycle"` includes **bikes & scooters**.

---

### **2⃣ YOLOv5 Not Downloading?**
If YOLOv5 fails to download automatically, install it manually:

```bash
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```

---

### **3⃣ Flask App Not Running?**
- Make sure you're using the correct Python version **(3.8+).**  
- If `flask` is missing, reinstall it:  
  ```bash
  pip install flask flask-cors
  ```

---

## 👨‍💻 Author
Developed by **[Your Name]** 🚀  
For questions, contact: [your_email@example.com]

---

## 📌 License
This project is **open-source** and free to use.  
Feel free to improve it! 🚀

