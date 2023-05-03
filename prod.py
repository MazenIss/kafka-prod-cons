from kafka import KafkaProducer
import json

KAFKA_TOPIC_NAME_CONS = "hello5"
KAFKA_BOOTSTRAP_SERVERS_CONS = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# convert the dictionary to a JSON string
json_data = json.dumps(data)
producer.send(KAFKA_TOPIC_NAME_CONS, json_data.encode('utf-8'))
producer.flush()
producer.close()
  

