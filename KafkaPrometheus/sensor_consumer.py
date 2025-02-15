from kafka import KafkaConsumer
from prometheus_client import start_http_server, Gauge
import json

# Define Prometheus metrics
temperature_metric = Gauge("sensor_temperature", "Temperature readings from sensor")
humidity_metric = Gauge("sensor_humidity", "Humidity readings from sensor")

# Start the Prometheus HTTP server on port 8000
start_http_server(8000)

# Create Kafka Consumer
consumer = KafkaConsumer(
    "sensor_data",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

print("Kafka Consumer started, waiting for messages...")

# Process messages from Kafka
for message in consumer:
    data = message.value
    temperature = data["temperature"]
    humidity = data["humidity"]

    # Update Prometheus metrics
    temperature_metric.set(temperature)
    humidity_metric.set(humidity)

    print(f"Received Data - Temperature: {temperature}, Humidity: {humidity}")
