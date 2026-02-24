from fastapi import FastAPI, File, UploadFile 
from base64 import b64encode

app = FastAPI(debug=True)

@app.post('/')
async def read_file(file: UploadFile = File(...)):
    data = await file.read()
    # return {'filename': file.filename}
    encoded_data = b64encode(data).decode('utf-8')
    print(type(encoded_data))
    return {
        "filename": file.filename,
        "content_type": file.content_type
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("ser:app", host="localhost", port=5000, reload=True)