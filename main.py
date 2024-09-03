from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host = os.getenv('HOST'), port =int(os.getenv('PORT')))
