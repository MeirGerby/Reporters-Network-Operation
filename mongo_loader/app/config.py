from pathlib import Path 
from typing import Optional 
from pydantic import Field, MongoDsn, TypeAdapter
from pydantic_settings import BaseSettings, SettingsConfigDict 

class GridFSConfig(BaseSettings):
    mongodb_uri: MongoDsn = Field(
        default=TypeAdapter(MongoDsn).validate_python("mongodb://localhost:27017"),
        validation_alias='MONGO_URI'
    ) 
    db_name: str = Field(default='files', validation_alias='MONGO_DB')
    gridfs_bucket: str = Field(default='fs', validation_alias="GRIDFS_BUCKET")

    temp_download_path: Path = Field(
        defalt=Path("./temp"),
        validation_alias="GRIDFS_TEMP_PATH"
    )     # type: ignore

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'
    ) 

    settings = GridFSConfig()