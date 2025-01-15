import pytest


@pytest.mark.asyncio
async def test_get_root(client):
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Go to /docs to see the API documentation."}




