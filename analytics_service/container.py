from messaging import KafkaConsumerWrapper, KafkaProducerWrapper 
from config import settings
from text_analizer import TextAnalyzer


class Manager:
    def __init__(self):
        self.clean_topic = settings.CLEAN_TEXT_KAFKA_TOPIC 
        self.analysed_topic = settings.ANALYTICS_TEXT_KAFKA_TOPIC
        self.bootstrap = settings.ANALYTICS_SERVICE_BOOTSTRAP_SERVERS 
        self.group_id = settings.ANALYTICS_SERVICE_GROUP_ID 
        self.producer: KafkaProducerWrapper = None   # type: ignore
        self.consumer: KafkaConsumerWrapper = None    # type: ignore 
        self.weapon_file = settings.WEAPON_LIST_FILE 

    async def set_up(self):
        self.producer = KafkaProducerWrapper(
            bootstrap_servers=self.bootstrap,
            topic=self.analysed_topic
        )

        self.consumer = KafkaConsumerWrapper(
            bootstrap_servers=self.bootstrap,
            group_id=self.group_id,
            topics= [self.clean_topic]   
        )   

    async def manage_text_analyser(self, text_analyser: TextAnalyzer):
        return text_analyser.analyse_text(self.weapon_file)
        

    async def run(self):
        await self.set_up()
        print("start the program")

        self.consumer.consumer_loop()
