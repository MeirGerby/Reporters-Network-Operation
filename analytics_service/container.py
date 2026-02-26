from messaging import KafkaConsumerWrapper, KafkaProducerWrapper 
from config import settings 


class Manager:
    def __init__(self):
        self.clean_topic = settings.CLEAN_TEXT_KAFKA_TOPIC 
        self.analysed_topic = settings.ANALYTICS_TEXT_KAFKA_TOPIC
        self.bootstrap = settings.ANALYTICS_SERVICE_BOOTSTRAP_SERVERS 
        self.group_id = settings.ANALYTICS_SERVICE_GROUP_ID 
        self.producer: KafkaProducerWrapper = None 
        self.consumer: KafkaConsumerWrapper = None 
    
    

    def set_up(self):
