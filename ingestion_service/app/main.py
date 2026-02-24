from .config import settings 
from .service.mongo_loader import MongoLoaderClient 
from .utils.read_data import ReadData 
from .kafka_producer.producer import KafkaEventProducer 
from .kafka_producer.evenv import Event 
from .utils.ocr import MetadataExtractor

class Manager:
    def __init__(self):
        self.data = ReadData(settings.FOLDER_PATH)
        self.path_list = self.data.read_images() 

        self.producer = KafkaEventProducer(brokers=[settings.KAFKA_BOOTSTRAP_SERVERS])
        self.topic = settings.KAFKA_TOPIC
        self.event_type = settings.EVENT_TYPE 

    def mongo_manager(self, img):
        mongo_loader = MongoLoaderClient(image=img)
        for img in self.path_list:
            try:
                respone = mongo_loader.send_to_mongo_loader() 
                print(respone)
            except ValueError as e:
                print(e, img) 
        # return respone


    def kafka_manager(self, payload): 
        event = Event(event_type=self.event_type, payload=payload) 
        self.producer.send(topic=self.topic, event=event)


    def main(self):
        for img_path in self.path_list:
            try:
            
                mongo_loader = MongoLoaderClient(image=img_path)
                mongo_response = mongo_loader.send_to_mongo_loader()
                print(f"Mongo Status: {mongo_response}")

                extractor = MetadataExtractor(path=img_path)
                extractor.read_text_from_image()
                text_data = extractor.get_text()


                self.kafka_manager(payload={"image_path": str(img_path), "ocr_text": text_data})
                
                print(f"Successfully processed: {img_path}")

            except Exception as e:
                print(f"Error processing {img_path}: {e}")
            self.producer.close()

if __name__ == '__main__':
    Manager().main()
 

