# tests/test_conversations.py
import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_create_conversation():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/conversations", json={"name": "Test", "model": "gpt-4o-mini"})
        assert response.status_code == 201
        assert "id" in response.json()
