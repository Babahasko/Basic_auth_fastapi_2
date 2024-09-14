from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
from api import router
from core.config import settings
from core.models import db_helper, Base

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    #startup
    yield
    #shutdown
    await db_helper.dispose()

main_app = FastAPI(
    lifespan=lifespan,
)
main_app.include_router(
    router,
#   prefix=settings.api.prefix,
)

if __name__ == "__main__":
    uvicorn.run(main_app, host = settings.run.host, port =settings.run.port)
