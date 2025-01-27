from fastapi import HTTPException
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from .models import Brand
from src.guitars.models import Guitar
from .scemas import BrandCreate, BrandUpdate, BrandUpdatePartial


async def get_brands(session: AsyncSession) -> list[Brand]:
    stmt = select(Brand).order_by(Brand.id).distinct()
    result: Result = await session.execute(stmt)
    brands = result.scalars().all()
    return list(brands)


async def get_brand_by_id(session: AsyncSession, brand_id: int) -> Brand | None:
    return await session.get(Brand, brand_id)


async def create_brand(session: AsyncSession, brand: BrandCreate) -> Brand:
    new_brand = Brand(**brand.model_dump())
    session.add(new_brand)
    await session.commit()
    return new_brand


async def delete_brand(session: AsyncSession, brand: Brand) -> None:
    await session.delete(brand)
    await session.commit()
    return True


async def get_brands_guitars(brand: Brand) -> list[Guitar]:
    return list(brand.guitars)


async def update_brand(
    brand_data: BrandUpdate | BrandUpdatePartial,
    brand: Brand,
    session: AsyncSession,
    partial: bool = False,
):
    for field, value in brand_data.model_dump(exclude_unset=partial).items():
        setattr(brand, field, value)
    await session.commit()
