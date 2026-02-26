from fastapi import UploadFile, File, HTTPException, Depends, APIRouter
from typing import Annotated
from bson import ObjectId

from config import settings
from service.grid_orchestrator import GridFSOrchestrator 
from repository.grid_fs_storage import GridFSStorage


router = APIRouter()


def get_orchestrator() -> GridFSOrchestrator:
    storage = GridFSStorage(settings)
    return GridFSOrchestrator(storage)

OrchestratorDep = Annotated[GridFSOrchestrator, Depends(get_orchestrator)]

@router.post("/upload-image/")
async def upload_image(
    orchestrator: OrchestratorDep,
    file: UploadFile = File(...)
):
    if not file.content_type.startswith("image/"):   # type: ignore
        raise HTTPException(status_code=400, detail="Only image uploads are allowed")

    try:
        content = await file.read()
        
        file_id = await orchestrator.process_and_store(
            file_content=content,
            filename=file.filename,    # type: ignore
            content_type=file.content_type
        )
        
        return {
            "message": "Image uploaded successfully",
            "file_id": file_id,
            "filename": file.filename
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

@router.get("/image-info/{file_id}")
async def get_image_info(file_id: str, orchestrator: OrchestratorDep):
    if not ObjectId.is_valid(file_id):
        raise HTTPException(status_code=400, detail="Invalid File ID format")
        
    metadata = await orchestrator.get_file_metadata(file_id)
    
    if not metadata:
        raise HTTPException(status_code=404, detail="Image not found")
        
    info = metadata[0]
    info["_id"] = str(info["_id"])
    return info

