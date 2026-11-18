
from fastapi import FastAPI
from app.api import health
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="Backend API for the Nova Retail platform",
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)

app.include_router(health.router)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to Nova Retail API",
        "status": "running",
    }
