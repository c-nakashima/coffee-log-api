import psycopg2
from psycopg2.extras import RealDictCursor
from app.core.config import DATABASE_URL


def get_conn():
    print("DB URL loaded?", bool(DATABASE_URL))
    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL is empty. Check .env path/loading.")
    return psycopg2.connect(
        DATABASE_URL,
        cursor_factory=RealDictCursor,
        sslmode="require",
    )