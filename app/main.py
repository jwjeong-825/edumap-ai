from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.routers.major import router as major_router

app = FastAPI()

app.include_router(major_router)


@app.get("/")
def home():
    return FileResponse("index.html")
