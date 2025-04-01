# 🚗 Vehicle Detection System

This project is a **Streamlit web application** that detects and classifies **vehicles** (cars, trucks, buses, motorcycles, bicycles) from uploaded videos using **YOLOv5**.

---

## 📌 Features
👉 Detects multiple vehicle types: **Cars, Trucks, Buses, Motorcycles, Bicycles**  
👉 Uses **YOLOv5** for object detection  
👉 **Streamlit web app** for easy video uploading & processing  
👉 **Real-time progress tracking** during video processing  
👉 **Processed video playback** with detected vehicles  
👉 **Download option** for processed videos  
👉 Supports **MP4, AVI, MOV, MKV** video formats  

---

## 📂 Project Structure
```
/vehicle-detection-system
│── /static                # Folder for storing uploaded & processed videos
│   │── /uploaded_videos   # Temporary storage for uploaded videos
│   │── /processed_videos  # Storage for processed videos with detections
│── streamlit_app.py       # Main Streamlit application
│── requirements.txt       # Project dependencies
│── README.md              # Project documentation
│── yolov5s.pt            # YOLOv5 model weights
```

---

## 🚀 Local Installation & Setup

### **1⃣ Clone the Repository**
```bash
git clone <repository-url>
cd vehicle-detection-system
```

### **2⃣ Install Dependencies**
Make sure you have **Python 3.8+** installed. Then, run:

```bash
pip install -r requirements.txt
```

---

### **3⃣ Run the Streamlit App**
```bash
streamlit run streamlit_app.py
```
After running the command, your browser will automatically open to the app, or you can visit:  
🔗 **http://localhost:8501/**

---

## 🌐 Streamlit Cloud Deployment

### **1⃣ Create a GitHub Repository**
1. Push your code to a GitHub repository
2. Make sure your repository includes:
   - streamlit_app.py
   - requirements.txt
   - yolov5s.pt model file
   - static folder structure

### **2⃣ Deploy on Streamlit Cloud**
1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository, branch, and set the main file path to `streamlit_app.py`
5. Click "Deploy"

### **3⃣ App Settings (Optional)**
- You can customize your app's name, theme, and other settings in the Streamlit Cloud dashboard
- For larger video files, you may need to adjust the memory settings in the Advanced Settings  

---

## 📅 How to Use
1. **Upload a video** via the web interface
2. Click the **Process Video** button
3. The system will **process the video** with a progress bar showing completion status
4. Once complete, the **processed video will be displayed** with labeled vehicles
5. You can **download the processed video** using the download button  

---

## 🎥 Video Processing Details
- Uses **YOLOv5 for vehicle detection**
- Saves processed videos in the **static/processed_videos/** directory
- **Green bounding boxes** are drawn around detected vehicles
- Vehicle counts are displayed at the top of the video  

---

## 🛠️ Troubleshooting

### **1⃣ Model Loading Issues**
If you encounter issues with the YOLOv5 model loading:
- Ensure the model file `yolov5s.pt` is in the correct location
- Check your internet connection as the model needs to download additional components on first run

### **2⃣ Video Processing Errors**
If video processing fails:
- Ensure the video format is supported (MP4, AVI, MOV, MKV)
- Try with a smaller video file as processing large videos requires more memory
- Check that you have sufficient disk space for the processed output

### **3⃣ Streamlit App Not Running**
- Make sure you're using the correct Python version **(3.8+)**
- If dependencies are missing, reinstall them:
  ```bash
  pip install -r requirements.txt
  ```

---

## 👨‍💻 Author
Developed by **karan rajput** 🚀  
For questions, contact: karanravirajput@gmail.com

---

## 📌 License
This project is **open-source** and free to use.  
Feel free to improve it! 🚀

