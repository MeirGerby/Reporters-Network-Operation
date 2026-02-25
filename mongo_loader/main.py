from fastapi import FastAPI 

from app.router.routes import router as upload_file_router

app = FastAPI(debug=True)
app.include_router(upload_file_router) 

def main():
    import uvicorn 
    uvicorn.run('main:app', host='localhost', port=5000, reload=True)

if __name__ == "__main__":
    main()

