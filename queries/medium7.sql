SELECT 
  category, 
  AVG(price) AS Avg_Price, 
  COUNT(*) AS Count 
FROM products 
GROUP BY category 
HAVING COUNT(*) >= 30
