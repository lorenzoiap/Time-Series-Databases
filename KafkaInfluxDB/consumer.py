from kafka import KafkaConsumer
import json

# Configurazione del consumer
consumer = KafkaConsumer(
    'sensor_data',  # Topic a cui sottoscriversi
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',  # Legge i messaggi dall'inizio del topic
    group_id='my-group',  # Identificativo del gruppo consumer
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))  # Deserializza i messaggi da JSON
)

print("Consumer avviato. In attesa di messaggi...")

for msg in consumer:
    print("Messaggio ricevuto:", msg.value)
