from confluent_kafka import Producer, Consumer 
import json 

class KafkaProducerWrapper:
    """kafka producer class"""
    def __init__(self, bootstrap_servers: str, topic: str):
        self.config = {"bootstrap.servers":bootstrap_servers }
        self.producer = Producer(self.config)   # type: ignore 
        self.topic = topic 

    async def send(self, message: dict):
        """send a message to kafka"""
        self.producer.produce(
            topic=self.topic,
            value=json.dumps(message).encode('utf-8')
        )

        self.producer.poll(0)

    def close(self):
        """close the connection"""
        self.producer.flush(10) 

class KafkaConsumerWrapper:
    def __init__(self, bootstrap_servers: str, topics: list, group_id: str):
        self.conf = {
            "bootstrap.servers": bootstrap_servers,
            "group.id": group_id,
            "auto.offset.reset": "earliest"
            }
        self.consumer = Consumer(self.conf)   # type: ignore
        self.topic = topics 

    
