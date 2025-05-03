import sqlite3


def get_conn():
    conn = sqlite3.connect("data/database.db")
    cur = conn.cursor()

    return conn, cur


def main():
    conn, cur = get_conn()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
        """
    )