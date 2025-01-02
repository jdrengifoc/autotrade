from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")

if not POLYGON_API_KEY:
    raise ValueError("POLYGON_API_KEY is not set. Please add it to your .env file.")
