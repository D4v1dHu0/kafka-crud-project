from kafka import KafkaConsumer
import json
import psycopg2

def insert_message(content):
    conn = psycopg2.connect(
        dbname = "kafkadb",
        user = "kafkauser",
        password = "kafkapass",
        host = "localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO messages (content) VALUES (%s);", (content,))
    conn.commit()
    cur.close()
    conn.close()

print("Consuming messages...")

consumer = KafkaConsumer(
    'messages',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='message-consumers',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for msg in consumer:
    try:
        print(f"Consumed: {msg.value}")
        insert_message(msg.value['message'])  # match the key in your JSON
    except Exception as e:
        print(f"Consumer error: {e}")