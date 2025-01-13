from typing import AsyncGenerator
from asyncio import current_task
from sqlalchemy.ext.asyncio import (
                create_async_engine, 
                async_sessionmaker, 
                AsyncSession,
                async_scoped_session,
                )
from app.core.config import settings



class DataBaseHelper():
    def __init__(self, url: str, echo: bool):
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_factory = async_sessionmaker(
            self.engine,
            autoflush=False, 
            autocommit=False, 
            expire_on_commit=False
            )
        
    def get_scoped_session(self):
        session = async_scoped_session(
            self.session_factory, 
            scopefunc=current_task,
        )
        return session
    
    async def session_dependency(self):
        async with self.session_factory() as session:
            yield session
            await session.close()
    

        
        
db_helper = DataBaseHelper(
    url=settings.db_url, 
    echo=settings.db_echo
)


