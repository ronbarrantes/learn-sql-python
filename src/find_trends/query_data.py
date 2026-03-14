from google.cloud import bigquery

client = bigquery.Client()

query = """
    SELECT 
        rank, 
        dma_name AS Name, 
        term, 
        refresh_date AS Day
    FROM 
        `bigquery-public-data.google_trends.top_rising_terms`
    ORDER BY Day Desc
    LIMIT 50
  """

def the_query():
    rows = client.query_and_wait(query)
    print("The query data:")
    for row in rows:
        print("name={}, day={}, rank={}".format(row["Name"], row["Day"], row["rank"]))

the_query()

