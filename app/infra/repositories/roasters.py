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
