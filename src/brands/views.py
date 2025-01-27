from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import db_helper
from .scemas import BrandCreate, Brand, BrandUpdate, BrandUpdatePartial
from src.guitars.scemas import Guitar
from . import crud
from .dependencies import brand_by_id


router = APIRouter()


@router.get("/brands", response_model=list[Brand])
async def get_brands(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_brands(session=session)


@router.post("/brands", response_model=Brand)
async def create_brand(
    brand: BrandCreate, session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.create_brand(session=session, brand=brand)


@router.get("/brands/{brand_id}", response_model=Brand)
async def get_brand_by_id(
    brand: Brand = Depends(brand_by_id),
):
    return brand


@router.get("/brands/{brand_id}/guitars", response_model=list[Guitar])
async def get_guitars_by_brand(
    brand: Brand = Depends(brand_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.get_brands_guitars(brand=brand)


@router.delete("/brands/{brand_id}")
async def delete_brand_by_id(
    brand: Brand = Depends(brand_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    await crud.delete_brand(session=session, brand=brand)
    return {"message": "Brand deleted successfully"}


@router.put("/brands/{brand_id}", response_model=Brand)
async def update_brand(
    brand_data: BrandUpdate,
    brand: Brand = Depends(brand_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    await crud.update_brand(brand_data=brand_data, brand=brand, session=session)
    return brand


@router.patch("/brands/{brand_id}", response_model=Brand)
async def partial_update_brand(
    brand_data: BrandUpdatePartial,
    brand: Brand = Depends(brand_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    await crud.update_brand(
        brand_data=brand_data, brand=brand, session=session, partial=True
    )
    return brand
