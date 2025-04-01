# WSGI configuration file for PythonAnywhere
import sys
import os

# Add the application directory to the Python path
path = os.path.dirname(os.path.abspath(__file__))
if path not in sys.path:
    sys.path.append(path)

# Import the Gradio app
from app_gradio import demo as application

# PythonAnywhere looks for an 'application' variable
# The Gradio demo is already defined as 'application' above