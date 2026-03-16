SELECT 
  status AS Status, 
  COUNT(status) AS Count 
FROM orders 
GROUP BY status
