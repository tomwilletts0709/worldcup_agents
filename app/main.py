from typing import Dict, Any
from fastapi import FastAPI, HTTPException, status, Request
from fastapi.middleware.cors import CORSMiddleware
from app.core.settings import settings
from app.core.limiter import limiter 
from app.core.logging import logger
from contextlib import asynccontextmanager
from datetime import datetime, timedelta
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    """ hand;e apploication startup and shutdown events """
    logger.info(
        "application starting up at %s", datetime.now().isoformat(), 
        project="main", 
        event="startup",
        version="1.0.0"
    )
    yield
    logger.info(
        "application shutting down at %s", datetime.now().isoformat(),
        project="main", event="shutdown", version="1.0.0"
    )

app = FastAPI(lifespan=lifespan)


app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





@app.get("/health")
@limiter.limit("10/minute")
async def health_check(request: Request)-> Dict[str, Any]:
    logger.info("health check called")
    return {"status": "ok", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
