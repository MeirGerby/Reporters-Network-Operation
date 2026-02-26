from confluent_kafka import Producer, Consumer 
import json 

class KafkaProducerWrapper:
    """kafka producer class"""
    def __init__(self, bootstrap_servers: str, topic: str):
        self.config = {"bootstrap.servers":bootstrap_servers }
        self.producer = Producer(self.config)   # type: ignore 
        self.topic = topic 

    
