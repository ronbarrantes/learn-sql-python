SELECT c.id, c.name, COUNT(o.id) AS 'Count'   
FROM customers AS c 
LEFT JOIN orders AS o ON c.id = o.customer_id 
GROUP BY c.id, c.name
ORDER BY Count Desc
