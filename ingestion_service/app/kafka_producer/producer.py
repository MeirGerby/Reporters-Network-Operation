from confluent_kafka import Producer
from .evenv import Event 

class KafkaEventProducer:
    def __init__(self, brokers: list[str]):
        self.config = {
            'bootstrap.servers': ",".join(brokers), 
            'retries': 5, 
            'linger.ms': 10
        }
        self._producer = Producer(self.config) 

    def send(self, topic: str, event: Event) -> None:

        self._producer.produce(
            topic=topic,
            value=event.to_json() 
        )

        self._producer.poll(0)

    def close(self) -> None:
        self._producer.flush()
