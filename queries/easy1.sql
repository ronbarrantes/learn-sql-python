-- 1) List the first 10 customers (id, name, city, joined_date), ordered by `joined_date` (oldest first).
--    - Focus: sorting and limiting results; core to almost every report.

SELECT 
  id, name, city, joined_date  
FROM customers
LIMIT 5
  
