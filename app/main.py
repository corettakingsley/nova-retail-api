
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.api import health, products, categories
from app.core.config import settings
from app.models import Product, Category

app = FastAPI(
    title=settings.APP_NAME,
    description="Backend API for the Nova Retail platform",
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(products.router)
app.include_router(categories.router)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to Nova Retail API",
        "status": "running",
    }
