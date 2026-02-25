import logging 
from pathlib import Path 
from typing import Optional 
from bson import ObjectId 

from app.repository.grid_fs_storage import GridFSStorage

logger = logging.getLogger(__name__) 

class GridFSOrchestrator:
    def __init__(self, storage: GridFSStorage):
        self.storage = storage 

    async def process_and_store(self, file_content: bytes, filename: str, content_type: Optional[str] = None) -> str:
        try:
            logger.info(f"start a process to store the file: {filename}")

            temp_path = self.storage.config.temp_download_path / f"upload_{ObjectId()}_{filename}"
            temp_path.parent.mkdir(parents=True, exist_ok=True)

            with open(temp_path, "wb") as f:
                f.write(file_content)
            
            file_id = await self.storage.upload_from_path(temp_path, filename)

            temp_path.unlink()
            
            logger.info(f"the file stored successfully")
            return file_id 
        
        except Exception as e:
            logger.error(f"error in Orchestration process {str(e)}")
    
    async def get_file_metadata(self, file_id: str): 
        cursor = self.storage.db[f"{self.storage.config.gridfs_bucket}.files"].find({"_id": ObjectId(file_id)})
        return await cursor.to_list(length=1)