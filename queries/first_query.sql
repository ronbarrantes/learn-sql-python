SELECT 
    rank, 
    dma_name AS Name, 
    term, 
    refresh_date AS Day
FROM 
    `bigquery-public-data.google_trends.top_rising_terms`
ORDER BY Day Desc
LIMIT 50

