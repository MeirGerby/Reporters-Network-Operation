from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorGridFSBucket
from pathlib import Path

from config import GridFSConfig 

class GridFSStorage:
    def __init__(self, config: GridFSConfig):
        self.config = config 
        self.client = AsyncIOMotorClient(str(self.config.mongodb_uri))
        self.db = self.client[self.config.db_name]
        self.fs = AsyncIOMotorGridFSBucket(self.db, bucket_name=self.config.gridfs_bucket)

    async def upload_from_path(self, file_path: Path, filename: str = None) -> str:  # type: ignore
        if not file_path.exists(): 
            raise FileNotFoundError(f"the file in {file_path} doesn't exists")

        name = filename or file_path.name 
        with open(file_path, 'rb') as source_file:
            file_id = await self.fs.upload_from_stream(
                filename=name,
                source=source_file,
                metadata={"original_path": str(file_path)}
            )
        
        return str(file_id) 
    
    async def download_to_path(self, file_id, destination_path: Path):
        destination_path.parent.mkdir(parents=True, exist_ok=True) 

        with open(destination_path, 'wb') as target_file:
            await self.fs.download_to_stream(file_id=file_id, destination=target_file)

        return destination_path 
    
    async def delete_file(self, file_id): 
        await self.fs.delete(file_id)

