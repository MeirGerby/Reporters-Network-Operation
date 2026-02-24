from pydantic_settings import BaseSettings, SettingsConfigDict 
from pathlib import Path

class Settings(BaseSettings):
    FOLDER_PATH: Path = Path("ingestion_service/data/tweet_images")
    MONGO_LOADER_URL: str = 'http://localhost:5000'

    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"
    KAFKA_TOPIC: str =  ""
    KAFKA_GROUP_ID: str = "" 

    EVENT_TYPE: str = "IMAGE_PROCESSED"

    model_config = SettingsConfigDict(
        env_file='.env'
    )

settings = Settings()
