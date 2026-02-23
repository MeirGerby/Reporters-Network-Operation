from pydantic_settings import BaseSettings, SettingsConfigDict 
from pathlib import Path

class Settings(BaseSettings):
    FOLDER_PATH: Path = Path("ingestion_service/data/tweet_images")

    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"
    KAFKA_ORDERS_TOPIC: str =  "pizza-orders"
    KAFKA_GROUP_ID: str = "text-team"

    model_config = SettingsConfigDict(
        env_file='.env'
    )

settings = Settings()
