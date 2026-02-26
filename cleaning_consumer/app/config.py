from pydantic_settings import BaseSettings 

class CleanConfig(BaseSettings):
    CLEAN_SERVICE_BOOTSTRAP_SERVERS: str = 'localhost:9092'
    CLEAN_SERVICE_GROUP_ID: str = "analyse-text" 
    ROW_TEXT_KAFKA_TOPIC: str =  "ROW" 
    CLEAN_TEXT_KAFKA_TOPIC: str =  "CLEAN" 

settings = CleanConfig()