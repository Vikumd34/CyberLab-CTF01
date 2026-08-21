import sqlite3
from pathlib import Path


DATABASE_PATH = Path(__file__).parent.parent / "database" / "ctf.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS challenges (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            points INTEGER NOT NULL,
            description TEXT NOT NULL,
            flag TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()
    
def add_initial_challenge():
    connection = get_connection()

    connection.execute("""
        INSERT INTO challenges
        (title, category, difficulty, points, description, flag)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        "The Hidden Door",
        "Reconnaissance",
        "Easy",
        100,
        "Find the hidden entry point of the target.",
        "CLCTF{recon_hidden_door}"
    ))

    connection.commit()
    connection.close()

if __name__ == "__main__":
    initialize_database()
    add_initial_challenge()
    print("Database initialized successfully.")
    print("Initial challenge added.")
    