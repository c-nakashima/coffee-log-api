import os
import re
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

# load .env in the same directory with main.py
env_path = Path(__file__).with_name(".env")
load_dotenv(env_path)

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")