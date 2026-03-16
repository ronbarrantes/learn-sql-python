-- 2) Show all products in the `Electronics` category with price > 100, ordered by price descending.

--  id INTEGER PRIMARY KEY,
--  name TEXT NOT NULL,
--  category TEXT NOT NULL,
--  price REAL NOT NULL

SELECT * 
FROM products
WHERE 
  category = "Electronics"
  AND
  price > 100
ORDER BY price Desc

