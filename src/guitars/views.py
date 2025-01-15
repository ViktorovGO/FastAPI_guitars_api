from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import db_helper
from .scemas import GuitarCreate, Guitar, GuitarUpdate, GuitarUpdatePartial
from src.brands.scemas import Brand
from . import crud
from .dependencies import guitar_by_id


router = APIRouter()

@router.get("/guitars", response_model=list[Guitar])
async def get_guitars(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_guitars(session=session)


@router.post("/guitars", response_model=Guitar)
async def create_guitar(
    guitar_data: GuitarCreate,
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.create_guitar(session=session, guitar_data=guitar_data)


@router.get("/guitars/{guitar_id}", response_model=Guitar)
async def get_guitar_by_id(
    guitar: Guitar = Depends(guitar_by_id)
):  
    return guitar


    
@router.get("/guitars/{guitar_id}/brand", response_model=Brand)
async def get_brand_of_guitar(
    guitar: Guitar = Depends(guitar_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    brand = await crud.get_brand_of_guitar(session=session, guitar=guitar)
    return brand


@router.delete("/guitars/{guitar_id}")
async def delete_guitar_by_id(
    guitar: Guitar = Depends(guitar_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    await crud.delete_guitar(session=session, guitar=guitar)
    return {"message": "Guitar deleted successfully"}


@router.put("/guitars/{guitar_id}", response_model=Guitar)
async def update_guitar(
    guitar_data: GuitarUpdate,
    guitar: Guitar = Depends(guitar_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),

):
    await crud.update_guitar(guitar_data=guitar_data, guitar=guitar, session=session)
    return guitar


@router.patch("/guitars/{guitar_id}", response_model=Guitar)
async def partial_update_guitar(
    guitar_data: GuitarUpdatePartial,
    guitar: Guitar = Depends(guitar_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    await crud.update_guitar(guitar_data=guitar_data, guitar=guitar, session=session, partial=True)
    return guitar

    


