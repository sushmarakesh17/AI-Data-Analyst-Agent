import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Supported file types
ALLOWED_FILE_TYPES = ["csv", "xlsx"]

# Upload settings
MAX_FILE_SIZE_MB = 200

# Output folders
REPORTS_DIR = "outputs/reports"
CHARTS_DIR = "outputs/charts"
CLEANED_DATA_DIR = "outputs/cleaned_data"

# App Settings
APP_TITLE = "AI Data Analyst"
PAGE_ICON = "📊"
LAYOUT = "wide"