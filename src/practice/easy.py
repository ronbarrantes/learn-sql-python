import sqlite3
from pathlib import Path

DB_PATH = Path("data/practice.db")
ch1 = Path("queries/easy1.sql").read_text()
conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row


def challege1():

    cursor = conn.cursor()
    cursor.execute(ch1)

    rows = cursor.fetchall()
    print("The query data:")
    for row in rows:
        print(
            "{} | {} from {} since {}".format(
                row["id"], row["name"], row["city"], row["joined_date"]
            )
        )
