import uvicorn
import logging
from fastapi import FastAPI, HTTPException
from src.core import settings
from src.guitars import guitar_router
from src.brands import brand_router
from src.scripts import get_guitars, update_guitars


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


@app.post("/update-db", tags=["Update DB"])
async def update_db():
    try:
        guitars = await get_guitars()
        await update_guitars(guitars)
    except:
        return HTTPException(status_code=500, detail="Database update failure.")
    raise HTTPException(status_code=200, detail="Database updated.")


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.run.host, port=settings.run.port, reload=True)

"""
gunicorn main:app --workers --worker-class \
    uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
"""
