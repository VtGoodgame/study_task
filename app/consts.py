from dotenv import load_dotenv
import os
load_dotenv()

api_version = os.getenv("VERSION", "1.0.0")
