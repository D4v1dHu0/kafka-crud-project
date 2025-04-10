from confluent_kafka import Producer
#import socket

# kafka config
conf = {
    'bootstrap.servers' : 'localhost:9092'
#    'client.id' : socket.gethostname()
}

# producer instance
producer = Producer(conf)

# Callback for delivery reports

def delivery_report(err, msg):
    if err is not None:
        print(f"Message didn't send: {err}")
    else:
        print(f"Message sent to {msg.topic()} [{msg.partition()}]")

# produce msg to the test topic

topic = 'test-topic'
producer.produce(topic, key = "key1", value = "Hello Kafka!", callback = delivery_report)
producer.flush()
    
print("Producer is done sending messages.")