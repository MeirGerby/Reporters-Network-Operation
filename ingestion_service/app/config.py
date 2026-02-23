from pydantic_settings import BaseSettings, SettingsConfigDict 

class Settings(BaseSettings):
    FOLDER_PATH: str = "ingestion_service/data/tweet_images"

    model_config = SettingsConfigDict(
        env_file='.env'
    )

settings = Settings()
