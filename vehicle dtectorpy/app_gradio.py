import gradio as gr
import os
import uuid
import cv2
from detect import detect_vehicles
from werkzeug.utils import secure_filename

# Define upload and output folders
UPLOAD_FOLDER = "static/uploaded_videos"
OUTPUT_FOLDER = "static/processed_videos"
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv'}

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_video(video):
    if video is None:
        return None, "No video uploaded. Please upload a video file."
    
    try:
        # Get the file extension
        file_extension = os.path.splitext(video)[1].lower()[1:]
        
        if file_extension not in ALLOWED_EXTENSIONS:
            return None, f"File type not allowed. Please upload: {', '.join(ALLOWED_EXTENSIONS)}"
        
        # Create a unique filename to avoid conflicts
        original_filename = os.path.basename(video)
        unique_filename = f"{uuid.uuid4()}_{original_filename}"
        video_path = os.path.join(UPLOAD_FOLDER, unique_filename)
        output_filename = f"processed_{unique_filename}"
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)
        
        # Copy the uploaded file to our upload folder
        import shutil
        shutil.copy(video, video_path)
        
        # Process the video
        detect_vehicles(video_path, output_path)
        
        # Get relative path for display
        relative_output_path = os.path.join("static", "processed_videos", output_filename)
        
        # Return the processed video path and a success message
        vehicle_counts = "Vehicles detected and counted successfully!"
        return relative_output_path, f"Video processed successfully! {vehicle_counts}"
    except Exception as e:
        return None, f"Error processing video: {str(e)}"

# Create Gradio interface
with gr.Blocks(title="Vehicle Detection System", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # 🚗 Vehicle Detection System
        
        Upload a video to detect and count vehicles. The system detects cars, trucks, buses, motorcycles, and bicycles.
        
        Supported formats: MP4, AVI, MOV, MKV
        """
    )
    
    with gr.Row():
        with gr.Column(scale=1):
            input_video = gr.Video(label="Upload Video", sources=["upload"], format="mp4")
            process_btn = gr.Button("Process Video", variant="primary")
            file_info = gr.Textbox(label="File Information", interactive=False)
        
        with gr.Column(scale=1):
            output_video = gr.Video(label="Processed Video with Detections")
            output_message = gr.Textbox(label="Status", interactive=False)
            
    # Update file info when video is uploaded
    def update_file_info(video):
        if video is None:
            return "No file selected"
        filename = os.path.basename(video)
        size_mb = os.path.getsize(video) / (1024 * 1024)
        return f"File: {filename}\nSize: {size_mb:.2f} MB"
    
    input_video.change(
        fn=update_file_info,
        inputs=[input_video],
        outputs=[file_info]
    )
    
    process_btn.click(
        fn=process_video,
        inputs=[input_video],
        outputs=[output_video, output_message]
    )
    
    gr.Markdown(
        """
        ## How it works
        
        1. Upload a video using the interface above
        2. Click 'Process Video' to start detection
        3. The system will detect and count vehicles in the video
        4. The processed video will show bounding boxes around detected vehicles
        
        This application uses YOLOv5 for object detection.
        """
    )

if __name__ == "__main__":
    # Print startup message
    print("\n🚗 Starting Vehicle Detection System with Gradio interface...")
    print(f"📁 Upload folder: {UPLOAD_FOLDER}")
    print(f"📁 Output folder: {OUTPUT_FOLDER}")
    print("✅ System is ready! Launching web interface...\n")
    
    # Launch the Gradio interface
    demo.launch(share=False, server_name="127.0.0.1")