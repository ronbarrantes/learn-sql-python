import sqlite3
from pathlib import Path

DB_PATH = Path("data/practice.db")
ch1 = Path("queries/easy1.sql").read_text()
ch2 = Path("queries/easy2.sql").read_text()
ch3 = Path("queries/easy3.sql").read_text()

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row


def challege1():
    cursor = conn.cursor()
    cursor.execute(ch1)

    rows = cursor.fetchall()
    print("CHALLEGE 1:")
    for row in rows:
        print(
            "{} | {}, from {}, joined on {}".format(
                row["id"], row["name"], row["city"], row["joined_date"]
            )
        )


def challege2():
    cursor = conn.cursor()
    cursor.execute(ch2)

    rows = cursor.fetchall()
    print("CHALLEGE 2:")
    for row in rows:
        print(
            "{} | {} - price: {} - {}".format(
                row["id"], row["name"], row["price"], row["category"]
            )
        )


def challege3():
    cursor = conn.cursor()
    cursor.execute(ch3)

    rows = cursor.fetchall()
    print("CHALLEGE 3:")
    for row in rows:
        print("{} | {} ".format(row["Status"], row["Count"]))
