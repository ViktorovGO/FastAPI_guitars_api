import pytest
import asyncio
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from src.main import app
from src.core import settings
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis


@pytest_asyncio.fixture()
async def client() -> AsyncClient:
    return AsyncClient(transport=ASGITransport(app=app), base_url="http://testserver")


@pytest.fixture(autouse=True)
def fastapi_cache():
    redis = aioredis.from_url(settings.redis.redis_url)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()
