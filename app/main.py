from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.settings import settings
from users.router import router as router_users


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], 
    allow_credentials=True,
    allow_methods=['*'],  
    allow_headers=['*'],  
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(router_users)