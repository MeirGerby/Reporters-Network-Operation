from messaging import KafkaConsumerWrapper, KafkaProducerWrapper 
from text_cleaner import TextCleaner
from config import settings
import asyncio 

class Manager():
    def __init__(self):
        self.bootstrap_server = settings.CLEAN_SERVICE_BOOTSTRAP_SERVERS
        self.group_id = settings.CLEAN_SERVICE_GROUP_ID 
        self.row_topic = settings.ROW_TEXT_KAFKA_TOPIC 
        self.clean_topic = settings.CLEAN_TEXT_KAFKA_TOPIC 
        self.consumer: KafkaConsumerWrapper  = None   # type: ignore
        self.producer: KafkaProducerWrapper = None       # type: ignore


    async def setup(self):
        """create the cunsumer and pruducer instances """
        self.consumer = KafkaConsumerWrapper(
            bootstrap_servers=self.bootstrap_server,
            group_id=self.group_id,
            topics=[self.row_topic]
        )

        self.producer = KafkaProducerWrapper(
            bootstrap_servers=self.bootstrap_server,
            topic=self.clean_topic
        )
    
    async def handle_messeges(self, data: dict):
        """get a dict from consumer and handle the text by cleaning it"""
        try:
            base_text = data.get('text', '') 
            text_cleaner: TextCleaner = TextCleaner(base_text)
            text_after_cleaning = await self.clean_text(text_cleaner)

            await self.producer.send({"cleaned_text": text_after_cleaning})
        except Exception as e:
            print("The proccesed faild {e}")
    
    async def clean_text(self, cleaner: TextCleaner):
        """clean text punctuation"""
        return cleaner.clean_text_pucnt() 
    
    async def run(self):
        await self.setup() 
        print("the program set up successfully")

        await self.consumer.consume_loop(self.handle_messeges)

    
    async def main(self):
        await self.run()
        
if __name__ == "__main__":
    manager = Manager()
    try:
        asyncio.run(manager.main()) 
    except KeyboardInterrupt:
        print(f"proccess stoped by user")
