from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import os

from dotenv import load_dotenv
from pathlib import Path

# load .env in the same directory with main.py
env_path = Path(__file__).with_name(".env")
load_dotenv(env_path)

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")

def get_conn():
    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL is empty. Check .env path/loading.")
    return psycopg2.connect(
        DATABASE_URL,
        cursor_factory=RealDictCursor,
        sslmode="require",
    )

@app.get("/roasters")
def get_roasters():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM roasters ORDER BY name ASC;")
    roasters = cur.fetchall()
    cur.close()
    conn.close()
    return roasters
