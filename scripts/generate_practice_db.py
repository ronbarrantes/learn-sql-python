import random
import sqlite3
from datetime import date, timedelta
from pathlib import Path

DB_PATH = Path("data/practice.db")

random.seed(7)

first_names = [
    "Ava", "Noah", "Liam", "Emma", "Olivia", "Mia", "Ethan", "Sofia", "Lucas", "Amelia",
    "Mason", "Isabella", "Logan", "Harper", "James", "Evelyn", "Elijah", "Abigail", "Henry", "Ella",
]
last_names = [
    "Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin",
    "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall",
]

categories = ["Books", "Electronics", "Home", "Outdoors", "Clothing"]
product_names = [
    "Notebook", "Headphones", "Coffee Mug", "Backpack", "Desk Lamp", "Water Bottle", "Bluetooth Speaker",
    "Sweater", "Tent", "Cookbook", "Monitor", "Keyboard", "Mouse", "Jacket", "Flashlight",
    "Sunglasses", "Running Shoes", "Yoga Mat", "Planner", "Camera Bag",
]

cities = ["New York", "Chicago", "Seattle", "Austin", "Denver", "Boston", "Phoenix", "Atlanta"]

DB_PATH.parent.mkdir(parents=True, exist_ok=True)
if DB_PATH.exists():
    DB_PATH.unlink()

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.executescript(
    """
    CREATE TABLE customers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        city TEXT NOT NULL,
        joined_date TEXT NOT NULL
    );

    CREATE TABLE products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL
    );

    CREATE TABLE orders (
        id INTEGER PRIMARY KEY,
        customer_id INTEGER NOT NULL,
        order_date TEXT NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
    );

    CREATE TABLE order_items (
        id INTEGER PRIMARY KEY,
        order_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        FOREIGN KEY (order_id) REFERENCES orders(id),
        FOREIGN KEY (product_id) REFERENCES products(id)
    );
    """
)

# Customers
customers = []
start_date = date(2023, 1, 1)
for i in range(1, 51):
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    city = random.choice(cities)
    joined = start_date + timedelta(days=random.randint(0, 600))
    customers.append((i, name, city, joined.isoformat()))

cur.executemany("INSERT INTO customers VALUES (?, ?, ?, ?)", customers)

# Products
products = []
for i in range(1, 81):
    name = f"{random.choice(product_names)} {i}"
    category = random.choice(categories)
    price = round(random.uniform(8, 220), 2)
    products.append((i, name, category, price))

cur.executemany("INSERT INTO products VALUES (?, ?, ?, ?)", products)

# Orders
statuses = ["pending", "shipped", "delivered", "cancelled"]
orders = []
order_start = date(2023, 6, 1)
for i in range(1, 201):
    customer_id = random.randint(1, 50)
    order_date = order_start + timedelta(days=random.randint(0, 300))
    status = random.choices(statuses, weights=[10, 30, 50, 10], k=1)[0]
    orders.append((i, customer_id, order_date.isoformat(), status))

cur.executemany("INSERT INTO orders VALUES (?, ?, ?, ?)", orders)

# Order items
order_items = []
item_id = 1
for order_id in range(1, 201):
    for _ in range(random.randint(1, 5)):
        product_id = random.randint(1, 80)
        quantity = random.randint(1, 4)
        order_items.append((item_id, order_id, product_id, quantity))
        item_id += 1

cur.executemany("INSERT INTO order_items VALUES (?, ?, ?, ?)", order_items)

conn.commit()
conn.close()

print(f"Wrote {DB_PATH}")
