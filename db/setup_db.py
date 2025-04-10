# script for db setup

import psycopg2

conn = psycopg2.connect( # NOT SECURE, might be good to put pswrd elsewhere
    dbname = "postgres",
    user = "postgres",
    password = "mysecretpassword",
    host = "localhost",
    port="5432"
)

cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id SERIAL PRIMARY KEY,
        content TEXT NOT NULL  
    );
""")

conn.commit()
cur.close()
conn.close()