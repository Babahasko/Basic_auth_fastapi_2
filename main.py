from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
from router import api_router
from config import settings
import os

load_dotenv()

app = FastAPI()
app.include_router(
    api_router,
    prefix = settings.api.prefix,
)

if __name__ == "__main__":
    uvicorn.run(app, host = settings.run.host, port =settings.run.port)
