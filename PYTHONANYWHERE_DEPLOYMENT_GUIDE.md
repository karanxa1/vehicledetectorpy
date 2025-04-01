# PythonAnywhere Deployment Guide for Vehicle Detection System

This guide will walk you through deploying the Vehicle Detection System on PythonAnywhere's free tier.

## Prerequisites

- A PythonAnywhere account (free tier is sufficient)
- Your Vehicle Detection System code (already prepared for deployment)

## Step 1: Create a PythonAnywhere Account

1. Go to [PythonAnywhere](https://www.pythonanywhere.com/) and sign up for a free account if you don't have one already.
2. Log in to your PythonAnywhere account.

## Step 2: Upload Your Code

1. In the PythonAnywhere dashboard, click on the "Files" tab.
2. Create a new directory for your project (e.g., `vehicledetector`).
3. Upload your project files to this directory. You can either:
   - Use the PythonAnywhere file uploader for individual files
   - Or use the Bash console to clone from a Git repository if your code is on GitHub

## Step 3: Set Up a Virtual Environment

1. Go to the "Consoles" tab and start a new Bash console.
2. Navigate to your project directory:
   ```bash
   cd vehicledetector
   ```
3. Create a virtual environment:
   ```bash
   mkvirtualenv --python=python3.9 venv_vehicledetector
   ```
4. Activate the virtual environment (if not already activated):
   ```bash
   workon venv_vehicledetector
   ```
5. Install the required packages:
   ```bash
   pip install -r "vehicle dtectorpy/requirements.txt"
   ```

## Step 4: Configure the Web App

1. Go to the "Web" tab in the PythonAnywhere dashboard.
2. Click on "Add a new web app".
3. Choose the domain name (it will be in the format `yourusername.pythonanywhere.com`).
4. Select "Manual configuration" (not "Flask").
5. Choose Python 3.9 as your Python version.

## Step 5: Configure WSGI File

1. In the web app configuration page, look for the "Code" section.
2. Click on the link to the WSGI configuration file (e.g., `/var/www/yourusername_pythonanywhere_com_wsgi.py`).
3. Replace the contents with the following (adjust paths as needed):

```python
import sys
import os

# Add your project directory to the path
path = '/home/yourusername/vehicledetector/vehicle dtectorpy'
if path not in sys.path:
    sys.path.append(path)

# Import the application
from wsgi_app import application
```

## Step 6: Configure Static Files

1. In the web app configuration page, scroll down to the "Static files" section.
2. Add the following static file mapping:
   - URL: `/static/`
   - Directory: `/home/yourusername/vehicledetector/static/`

## Step 7: Set Environment Variables

1. In the web app configuration page, scroll to the "Environment variables" section.
2. Add the following environment variable:
   - Name: `PYTHONPATH`
   - Value: `/home/yourusername/vehicledetector`

## Step 8: Reload the Web App

1. Scroll to the top of the web app configuration page.
2. Click the green "Reload" button.

## Step 9: Test Your Application

1. Once the reload is complete, visit your application at `yourusername.pythonanywhere.com`.
2. You should see the Vehicle Detection System interface.

## Troubleshooting

### Error Logs

If your application doesn't work as expected, check the error logs:

1. Go to the "Web" tab.
2. Scroll down to the "Logs" section.
3. Check both the "Error log" and "Server log" for any issues.

### Common Issues

- **File Permissions**: Ensure all directories have the correct permissions.
- **Path Issues**: Double-check all file paths in your code and WSGI configuration.
- **Package Installation**: Make sure all required packages are installed in your virtual environment.
- **Model Loading**: If the YOLOv5 model fails to load, check the path and ensure it's accessible.

### Resource Limitations

Be aware that PythonAnywhere's free tier has resource limitations:

- CPU time is limited
- Outbound network access is restricted to whitelisted sites
- Storage space is limited

For processing large videos, you might need to upgrade to a paid plan.

## Maintenance

- Free PythonAnywhere accounts require you to log in at least once every three months to keep your web app active.
- To update your application, upload the new files and reload the web app.

## Additional Resources

- [PythonAnywhere Help Pages](https://help.pythonanywhere.com/)
- [PythonAnywhere Forums](https://www.pythonanywhere.com/forums/)