from flask import Flask, render_template, request, send_from_directory, url_for
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os
from detect import detect_vehicles  # Import the updated function

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

UPLOAD_FOLDER = 'static/'  # Directory to store videos
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
    return render_template('upload.html', processed_video=None)

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return "No file uploaded!", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file!", 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        processed_path = os.path.join(app.config['UPLOAD_FOLDER'], 'processed_video.mp4')
        
        file.save(input_path)  # Save original video
        detect_vehicles(input_path, processed_path)  # Process video for vehicle detection
        
        return render_template('upload.html', processed_video=url_for('serve_video', filename='processed_video.mp4'))
    else:
        return "Invalid file type!", 400

@app.route('/video/<filename>')
def serve_video(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, mimetype='video/mp4')

if __name__ == '__main__':
    app.run(debug=True)
