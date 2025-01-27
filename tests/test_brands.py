import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_brands(client: AsyncClient):
    response = await client.get("api/v1/brands")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_create_delete_brand(client: AsyncClient):
    response = await client.post(
        "api/v1/brands",
        json={
            "name": "test",
        },
    )
    assert response.status_code == 200
    assert response.json()["name"] == "test"

    brand_id = response.json()["id"]
    response = await client.delete(f"api/v1/brands/{brand_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Brand deleted successfully"}


@pytest.mark.asyncio
async def test_create_brand_empty(client: AsyncClient):
    response = await client.post(
        "api/v1/brands",
        json={
            "name": "",
        },
    )
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_create_brand_too_long(client: AsyncClient):
    response = await client.post(
        "/api/v1/brands",
        json={
            "name": "a" * 21,
        },
    )
    assert response.status_code == 422
