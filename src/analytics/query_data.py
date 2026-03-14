from pathlib import Path

from google.cloud import bigquery

sql_text = Path("queries/first_query.sql").read_text()

client = bigquery.Client()

query = sql_text 

def the_query():
    rows = client.query_and_wait(query)
    print("The query data:")
    for row in rows:
        print("name={}, day={}, rank={}".format(row["Name"], row["Day"], row["rank"]))

the_query()

