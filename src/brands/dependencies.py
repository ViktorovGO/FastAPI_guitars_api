from fastapi import Depends, Path, HTTPException
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import db_helper
from .models import Brand


async def brand_by_id(
    brand_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Brand:
    brand = await session.get(Brand, brand_id)
    if brand is not None:
        return brand

    raise HTTPException(status_code=404, detail="Brand not found")
