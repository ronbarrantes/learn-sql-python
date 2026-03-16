import random
import sqlite3
from datetime import date, timedelta
from pathlib import Path

DB_PATH = Path("data/practice.db")

random.seed(7)

first_names = [
    "Ava", "Noah", "Liam", "Emma", "Olivia", "Mia", "Ethan", "Sofia", "Lucas", "Amelia",
    "Mason", "Isabella", "Logan", "Harper", "James", "Evelyn", "Elijah", "Abigail", "Henry", "Ella",
    "Benjamin", "Charlotte", "Daniel", "Scarlett", "Jack", "Luna", "Alexander", "Grace", "Sebastian",
    "Chloe", "David", "Penelope", "Joseph", "Riley", "Samuel", "Zoey", "Carter", "Nora", "Wyatt",
    "Hannah",
]
last_names = [
    "Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin",
    "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall",
    "Allen", "Young", "King", "Wright", "Scott", "Green", "Baker", "Adams", "Nelson", "Hill",
    "Campbell", "Mitchell", "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Torres",
    "Parker",
]

category_products = {
    "Books": [
        "Notebook", "Cookbook", "Planner", "Novel", "Travel Guide", "Journal", "Sketchbook",
        "Recipe Cards", "Study Guide",
    ],
    "Electronics": [
        "Headphones", "Bluetooth Speaker", "Monitor", "Keyboard", "Mouse", "Camera Bag",
        "Portable Charger", "Smartwatch", "Webcam", "Wireless Earbuds", "USB Hub", "Laptop Stand",
    ],
    "Home": [
        "Coffee Mug", "Desk Lamp", "Water Bottle", "Yoga Mat", "Throw Blanket", "Candle",
        "Picture Frame", "Kitchen Towels", "Storage Bin", "Cutting Board",
    ],
    "Outdoors": [
        "Backpack", "Tent", "Flashlight", "Sunglasses", "Camping Stove", "Hiking Poles",
        "Sleeping Bag", "Water Filter", "Trail Map",
    ],
    "Clothing": [
        "Sweater", "Jacket", "Running Shoes", "Raincoat", "Beanie", "Hoodie",
        "Athletic Socks", "Gloves",
    ],
}
categories = list(category_products.keys())

cities = [
    "New York", "Chicago", "Seattle", "Austin", "Denver", "Boston", "Phoenix", "Atlanta",
    "San Francisco", "Los Angeles", "Portland", "Dallas", "Houston", "Miami", "Minneapolis",
    "Philadelphia", "San Diego", "Charlotte", "Nashville", "Raleigh",
]

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
for i in range(1, 121):
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    city = random.choice(cities)
    joined = start_date + timedelta(days=random.randint(0, 600))
    customers.append((i, name, city, joined.isoformat()))

cur.executemany("INSERT INTO customers VALUES (?, ?, ?, ?)", customers)

# Products
products = []
for i in range(1, 161):
    category = random.choice(categories)
    name = f"{random.choice(category_products[category])} {i}"
    price = round(random.uniform(8, 220), 2)
    products.append((i, name, category, price))

cur.executemany("INSERT INTO products VALUES (?, ?, ?, ?)", products)

# Orders
statuses = ["pending", "shipped", "delivered", "cancelled"]
orders = []
order_start = date(2023, 6, 1)
for i in range(1, 401):
    customer_id = random.randint(1, 50)
    order_date = order_start + timedelta(days=random.randint(0, 300))
    status = random.choices(statuses, weights=[10, 30, 50, 10], k=1)[0]
    orders.append((i, customer_id, order_date.isoformat(), status))

cur.executemany("INSERT INTO orders VALUES (?, ?, ?, ?)", orders)

# Order items
order_items = []
item_id = 1
for order_id in range(1, 401):
    for _ in range(random.randint(1, 5)):
        product_id = random.randint(1, 160)
        quantity = random.randint(1, 4)
        order_items.append((item_id, order_id, product_id, quantity))
        item_id += 1

cur.executemany("INSERT INTO order_items VALUES (?, ?, ?, ?)", order_items)

conn.commit()
conn.close()

print(f"Wrote {DB_PATH}")
