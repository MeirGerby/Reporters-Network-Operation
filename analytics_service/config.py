from pydantic_settings import BaseSettings 

class AnalyticsConfig(BaseSettings):
    ANALYTICS_SERVICE_BOOTSTRAP_SERVERS: str = 'localhost:9092' 
    ANALYTICS_SERVICE_GROUP_ID: str = "analyse-text" 
    CLEAN_TEXT_KAFKA_TOPIC: str =  "CLEAN"  
    ANALYTICS_TEXT_KAFKA_TOPIC: str =  "ANALYTICS"  
    WEAPON_LIST_FILE: str = "data/weapon_list.txt"

settings = AnalyticsConfig()