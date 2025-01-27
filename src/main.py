import uvicorn
import logging
from fastapi import FastAPI
from src.core import settings
from src.guitars import guitar_router
from src.brands import brand_router


logging.basicConfig(
    format=settings.logging.log_format,
)


app = FastAPI(
    title="Guitar API",
    description="API for guitars and guitar brands",
)

app.include_router(guitar_router, tags=["Guitars"], prefix="/api/v1")
app.include_router(brand_router, tags=["Brands"], prefix="/api/v1")


@app.get("/", include_in_schema=False)
async def root():
    return {"message": "Go to /docs to see the API documentation."}


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.run.host, port=settings.run.port, reload=True)

"""
gunicorn main:app --workers --worker-class \
    uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
"""
