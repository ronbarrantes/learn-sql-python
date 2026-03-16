import sqlite3
from pathlib import Path

DB_PATH = Path("data/practice.db")
ch1 = Path("queries/easy1.sql").read_text()


def challege1():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(ch1)

    rows = cursor.fetchall()
    print("The query data:")
    for row in rows:
        print("id = {}".format(row["id"]))
