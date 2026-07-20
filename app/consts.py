import os
from dotenv import load_dotenv

load_dotenv()

VERSION = os.getenv("VERSION", "1.0.0")
APP_PORT = int(os.getenv("APP_PORT", 8080))

