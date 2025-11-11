"""
Centralized settings loader.

Why:
- All configurable values in one place.
"""
import os
from dotenv import load_dotenv
load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
TARGET_CHANNEL = os.getenv("TARGET_CHANNEL", "CAPPERS FREE")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://192.168.0.111:11434")
TESSERACT_LANGUAGE = os.getenv("TESSERACT_LANGUAGE", "eng")
