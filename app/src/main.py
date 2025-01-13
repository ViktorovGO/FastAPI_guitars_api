import uvicorn
from fastapi import FastAPI
from app.guitars import guitar_router
from app.brands import brand_router


app = FastAPI(
    title="Guitar API",
    description="API for guitars and guitar brands",
)

app.include_router(guitar_router, tags=['Guitars'])
app.include_router(brand_router, tags=['Brands'])

if __name__ == "__main__":
    uvicorn.run('app.src.main:app', host="0.0.0.0", port=8000, reload=True)