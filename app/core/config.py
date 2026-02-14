import os
from pathlib import Path
from dotenv import load_dotenv

# Access .env in the project root
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(env_path)

DATABASE_URL = os.getenv("DATABASE_URL")
