from confluent_kafka import Consumer
import psycopg2

consumer = Consumer({
    'bootstrap.servers' : 'localhost:9092',
    'group.id' : 'test-group',
    'auto.offset.reset' : 'earliest'   
})

consumer.subscribe(['test-topic'])

conn = psycopg2.connect( # NOT SECURE, might be good to put pswrd elsewhere
    dbname = "postgres",
    user = "postgres",
    password = "mysecretpassword",
    host = "localhost",
    port="5432"
)

cursor = conn.cursor()

print("COnsuming messages...")

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(f"COnsumer error: {msg.error()}")
        continue

    print(f"Received message: {msg.value().decode('utf-8')}")
    cursor.execute("INSERT INTO messages (content) VALUES (%s)" , (msg.value().decode('utf-8'),))
    conn.commit()