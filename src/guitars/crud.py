from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from .models import Guitar
from src.brands.models import Brand
from .scemas import GuitarCreate, GuitarUpdate, GuitarUpdatePartial


async def get_guitars(session: AsyncSession) -> list[Guitar]:
    stmt = select(Guitar).order_by(Guitar.id)
    result: Result = await session.execute(stmt)
    guitars = result.scalars().all()
    return list(guitars)


async def get_guitar_by_id(session: AsyncSession, guitar_id: int) -> Guitar | None:
    return await session.get(Guitar, guitar_id)


async def create_guitar(session: AsyncSession, guitar_data: GuitarCreate) -> Guitar:
    try:
        new_guitar = Guitar(**guitar_data.model_dump())
        session.add(new_guitar)
        await session.commit()
    except:
        raise HTTPException(status_code=400, detail="No brand with that id")
    else:
        return new_guitar


async def delete_guitar(session: AsyncSession, guitar: Guitar) -> bool:
    await session.delete(guitar)
    await session.commit()


async def get_brand_of_guitar(session: AsyncSession, guitar: Guitar) -> Brand:
    return guitar.brand


async def update_guitar(
    guitar_data: GuitarUpdate | GuitarUpdatePartial,
    guitar: Guitar,
    session: AsyncSession,
    partial: bool = False,
):
    for field, value in guitar_data.model_dump(exclude_unset=partial).items():
        setattr(guitar, field, value)
    try:
        await session.commit()
    except:
        raise HTTPException(status_code=400, detail="No brand with that id")
