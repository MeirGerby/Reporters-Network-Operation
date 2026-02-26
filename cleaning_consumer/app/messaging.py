from confluent_kafka import Producer, Consumer
import json


class KafkaProducerWrapper:
    def __init__(self, bootstrap_servers: str):
        self.conf = {'bootstrap.servers': bootstrap_servers}
        self.producer = Producer(self.conf)   # type: ignore

    async def send(self, topic: str, message: dict):
        
        self.producer.produce(
            topic, 
            value=json.dumps(message).encode('utf-8')
        )
        
        self.producer.poll(0)

    def close(self):
        self.producer.flush(10)


class KafkaConsumerWrapper:
    def __init__(self, bootstrap_servers: str, group_id: str, topics: list):
        self.conf = {
            'bootstrap.servers': bootstrap_servers,
            'group.id': group_id,
            'auto.offset.reset': 'earliest'
        }
        self.consumer = Consumer(self.conf)  # type: ignore
        self.topics = topics

    async def consume_loop(self, callback):
        self.consumer.subscribe(self.topics)
        try:
            while True:
                msg = self.consumer.poll(1.0)
                if msg is None: continue
                if msg.error():
                    print(f"Consumer error: {msg.error()}")
                    continue
                
                data = json.loads(msg.value().decode('utf-8'))  # type: ignore
                await callback(data)
        finally:
            self.consumer.close()

