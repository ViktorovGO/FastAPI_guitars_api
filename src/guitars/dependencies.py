from fastapi import Depends, Path, HTTPException
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import db_helper
from .models import Guitar


async def guitar_by_id(
    guitar_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Guitar:
    guitar = await session.get(Guitar, guitar_id)
    if guitar is not None:
        return guitar

    raise HTTPException(status_code=404, detail="Guitar not found")
