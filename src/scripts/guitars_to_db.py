import json
from src.db import db_helper
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from src.guitars.models import Guitar
from src.brands.models import Brand

with open("src/scripts/guitars.json", "r") as file:
    guitars = json.load(file)


async def guitars_to_db(session: AsyncSession, guitars: list):
    """Запись данных по гитарам в базу данных"""
    for obj in guitars:
        Brand_obj = Brand(name=obj.pop("brand"))
        brand = await session.execute(select(Brand).filter_by(name=Brand_obj.name))
        object = brand.scalars().first()
        if object is None:
            session.add(Brand_obj)
            await session.commit()
            brand_id = Brand_obj.id
        else:
            brand_id = object.id
        obj["brand_id"] = int(brand_id)
        obj["price"] = int(obj["price"])
        # Найдем существующую запись по уникальным полям (например, id или combination of fields)
        guitar = await session.execute(
            select(Guitar).filter_by(
                brand_id=obj["brand_id"],
                article=obj["article"],
            )
        )
        existing_guitar = guitar.scalars().first()
        if existing_guitar:
            await session.execute(
                update(Guitar)
                .where(Guitar.id == existing_guitar.id)
                .values({"price": obj["price"]})
            )
            await session.commit()
        else:
            # Если записи не найдено, создаём новую
            Guitar_obj = Guitar(**obj)
            session.add(Guitar_obj)
            await session.commit()


async def main():
    async for session in db_helper.session_dependency():
        await guitars_to_db(session, guitars)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
