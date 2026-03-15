# SQL Practice Tasks (SQLite)

Use `data/practice.db`. Tables: `customers`, `products`, `orders`, `order_items`.

## Easy
1) List the first 10 customers (id, name, city, joined_date), ordered by `joined_date` (oldest first).
   - Focus: sorting and limiting results; core to almost every report.
2) Show all products in the `Electronics` category with price > 100, ordered by price descending.
   - Focus: filtering with `WHERE` and basic sorting; essential for precise slices of data.
3) Count how many orders are in each `status`. Show `status` and the count.
   - Focus: `GROUP BY` for basic aggregation; foundational for summaries.
4) Find the 5 most recent orders (id, customer_id, order_date, status).
   - Focus: date sorting and limiting; common in recency-based analysis.

## Medium
5) For each customer, show total number of orders. Include customers with zero orders. Sort by total orders descending.
   - Focus: `LEFT JOIN` + aggregation; critical for “include missing” cases.
6) For each order, compute the total number of items (sum of `quantity`). Return order id and total items.
   - Focus: joining detail rows and aggregating; common in order/invoice logic.
7) For each product category, compute average price and number of products. Show only categories with at least 10 products.
   - Focus: aggregation with `HAVING`; used to filter groups by thresholds.

## Hard
8) Find customers who have ordered from at least 3 different product categories. Return customer id, name, and number of categories.
   - Focus: distinct counts across joins; useful for “breadth” analysis.
9) Find the top 5 customers by total spend (sum of `quantity * price`) for orders with `status = 'delivered'`.
   - Focus: multi-table joins with computed metrics; common for revenue questions.
10) Using a CTE, compute monthly order counts and then list months where the count is above the overall monthly average.
    - Focus: CTEs to structure multi-step logic; keeps complex queries readable.

## Advanced
11) Use a window function to rank each customer’s orders by date (most recent = 1). Show customer id, order id, order date, and rank.
    - Focus: window functions for per-group ranking without collapsing rows.
12) For each customer, compute the days between their first and most recent order. Use window functions.
    - Focus: window aggregates for per-customer metrics; avoids self-joins.
13) Find products that have never been ordered (anti-join pattern).
    - Focus: identifying “missing” relationships; essential for audits and QA.
14) For each product category, list the top 3 most ordered products (by total quantity). Use a window function.
    - Focus: top‑N per group; a frequent real-world reporting pattern.
15) Identify “streaks” of orders per customer: consecutive orders where the gap between orders is 7 days or fewer. Return customer id and streak length (define how you want to count it).
    - Focus: sequencing with `LAG/LEAD`; useful for behavior analysis.
