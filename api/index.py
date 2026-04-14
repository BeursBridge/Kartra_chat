# api/index.py
import sys
import os

# Adjust Python path to include the 'managed-chatkit' directory
# This allows importing modules from within 'managed-chatkit'
# The path should be relative to the root of your Vercel project.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the FastAPI 'app' instance from your managed-chatkit backend
# The full path to your FastAPI app within the managed-chatkit structure:
# managed-chatkit/backend/app/main.py
from managed_chatkit.backend.app.main import app as application

# Vercel expects an 'application' variable to be the entry point for Python functions.
