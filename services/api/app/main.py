from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import ai, catalog, integrations
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    catalog.router,
    prefix="/api/v1"
)

app.include_router(
    ai.router,
    prefix="/api/v1"
)

app.include_router(
    integrations.router,
    prefix="/api/v1"
)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "ayvora-api"
    }
