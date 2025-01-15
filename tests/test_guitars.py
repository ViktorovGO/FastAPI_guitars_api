import pytest   
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_guitars(client: AsyncClient):
    response = await client.get("api/v1/guitars")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_create_guitar(client: AsyncClient):
    response = await client.post("api/v1/guitars", json=
        { 
            "article": "string", 
            "brand_id": 0, 
            "title": "string", 
            "price": 0, 
        })
    assert response.status_code == 400  
    assert response.json() == { 
        "detail": "No brand with that id"
        }
    
    response = await client.post("api/v1/guitars", json=
        {
            "brand_id": 0,
            "title": "string",
            "price": 0
        })
    assert response.status_code == 422
    
        