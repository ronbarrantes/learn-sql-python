SELECT 
  order_id, 
  SUM(quantity) AS item_quantity 
FROM order_items 
GROUP BY order_id
