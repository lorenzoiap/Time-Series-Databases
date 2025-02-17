from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

topic = "sensor_data"

print("Producer avviato. Invio dei messaggi ogni 1 secondo...")

while True:
    data = {
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(40.0, 60.0), 2),
        "timestamp": time.time()
    }
    producer.send(topic, value=data)
    print(f"Sent: {data}")
    time.sleep(1)
