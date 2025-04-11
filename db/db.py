import psycopg2


def get_connection():
    return psycopg2.connect(
        dbname="kafkadb",
        user="kafkauser",
        password="kafkapass",
        host="localhost", # use "postgres" if inside container
        port="5432"
    )

def insert_message(content):
    with get_connection as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO message (content) VALUES (%s);",(content,))
        conn.commit()
        
def get_all_messages():
    with get_connection as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM message;")
            return cur.fetchall()
            
def update_message(id, new_content):
    with get_connection as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE message SET content = %s WHERE id = %s;",(new_content, id))
        conn.commit()
            
def delete_message(id):
    with get_connection as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM message WHERE id = %s;",(id,))
        conn.commit()