from messaging import KafkaConsumerWrapper, KafkaProducerWrapper 
from text_cleaner import TextCleaner
from config import settings


class Manager():
    def __init__(self):
        self.bootstrap_server = settings.CLEAN_SERVICE_BOOTSTRAP_SERVERS
        self.group_id = settings.CLEAN_SERVICE_GROUP_ID 
        self.topic = settings.ROW_TEXT_KAFKA_TOPIC 
        self.consumer: KafkaConsumerWrapper  = None   # type: ignore
        self.producer: KafkaProducerWrapper = None       # type: ignore


    async def setup(self):
        """create the cunsumer and pruducer instances """
        self.consumer = await KafkaConsumerWrapper(
            bootstrap_servers=self.bootstrap_server,
            group_id=self.group_id,
            topics=[self.topic]
        )

        self.producer = await KafkaProducerWrapper(
            bootstrap_servers=self.bootstrap_server,
        )
    
    async def handle_messeges(self, data: dict):
        """get a dict from consumer and handle the text by cleaning it"""
        text = data.get('text', '') 
        clean = self.clean_text(text)
        return await self.consumer.consume_loop(clean)
    
    async def clean_text(self, text):
        self.clean = TextCleaner(text=text) 
        return self.clean.clean_text_pucnt() 
    
    async def run(self):
        await self.setup() 
        print("the program set up successfully")

        await self.consumer.consume_loop(self.handle_messeges)

    
    async def main(self):
        await self.run()
        