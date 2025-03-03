from flask import Flask, render_template, request, send_from_directory
import os
import uuid
import threading
from werkzeug.utils import secure_filename
# Import detect_vehicles directly, not through import statement
from detect import detect_vehicles

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploaded_videos"
OUTPUT_FOLDER = "static/processed_videos"
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv'}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "No file uploaded", 400
    
    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400
    
    if not allowed_file(file.filename):
        return f"File type not allowed. Please upload: {', '.join(ALLOWED_EXTENSIONS)}", 400
    
    # Create a unique filename to avoid conflicts
    filename = secure_filename(file.filename)
    unique_filename = f"{uuid.uuid4()}_{filename}"
    video_path = os.path.join(app.config["UPLOAD_FOLDER"], unique_filename)
    output_filename = f"processed_{unique_filename}"
    output_path = os.path.join(app.config["OUTPUT_FOLDER"], output_filename)
    
    # Save the uploaded file
    file.save(video_path)
    
    # Process the video
    detect_vehicles(video_path, output_path)
    
    # Create a relative path for the template
    relative_output_path = f"processed_videos/{output_filename}"
    
    return render_template("result.html", processed_video=relative_output_path)

@app.route("/processed_videos/<filename>")
def processed_video(filename):
    return send_from_directory(app.config["OUTPUT_FOLDER"], filename)

if __name__ == "__main__":
    app.run(debug=True)