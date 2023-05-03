from kafka import KafkaConsumer

# Set up Kafka consumer
consumer = KafkaConsumer(
    'hello5',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group'
)

# Read messages from Kafka topic
for message in consumer:
    print(message.value.decode('utf-8'))