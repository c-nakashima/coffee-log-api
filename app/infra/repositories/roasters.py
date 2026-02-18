# import function to connect db
from app.infra.db.connection import get_conn


# Repository layer: talk to the database with SQL


def get_roasters():
    """
    fetch all roasters from the roasters table
    Returns a list og rows (dicts if RealDictCursor is used)
    """
    # Open a DB connection
    # Ensure it is cleand up properly after use (close, and commit/rollback depending on what happened)
    with get_conn() as conn:
        # Create a cursor for SQL execution
        # Ensure it is closed properly after use
        with conn.cursor() as cur:
            # execute SQL
            cur.execute("SELECT * FROM roasters ORDER BY name ASC;")
            # return dictionary
            return cur.fetchall()


def get_by_name_normalized(name_normalized: str):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, name, name_normalized
                FROM roasters
                WHERE name_normalized = %s
                LIMIT 1;
            """, (name_normalized,))

            return cur.fetchone()


def create_roaster(name: str, name_normalized: str):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO roasters (name, name_normalized)
                VALUES (%s, %s)
                RETURNING *;
                """,
                (name, name_normalized),
            )
            row = cur.fetchone()
            conn.commit()
            return row