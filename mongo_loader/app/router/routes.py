from fastapi import APIRouter, File, UploadFile

router = APIRouter() 


@router.post('/upload-file')
async def upload_file(file: UploadFile = File(...)):
    data = await file.read()