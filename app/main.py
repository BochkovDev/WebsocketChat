from fastapi import FastAPI

from core.settings import settings


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}