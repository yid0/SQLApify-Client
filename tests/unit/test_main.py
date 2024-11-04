import pytest
from unittest.mock import patch, AsyncMock
from fastapi.testclient import TestClient
from src.main import app, startup_event, main

client = TestClient(app)


@pytest.mark.asyncio
async def test_status_endpoint():
    with patch(
        "src.service.status.StatusService.handle_request", new_callable=AsyncMock
    ) as mock_handle:
        mock_handle.return_value = {"status": "OK"}

        response = client.get("/status")

        assert response.status_code == 200
        assert response.json() == {"status": "OK"}
        mock_handle.assert_awaited_once()


@pytest.mark.asyncio
async def test_startup_event_success():
    with patch(
        "src.service.user.UserService.handle_request", new_callable=AsyncMock
    ) as mock_user_handle, patch(
        "src.config.BodySettings.load",
        return_value={
            "database": "test_db",
            "username": "test_user",
            "password": "test_password",
        },
    ):
        mock_user_handle.return_value = {"status": "user_created"}

        await startup_event()

        mock_user_handle.assert_awaited_once()


@pytest.mark.asyncio
async def test_startup_event_failure():
    with patch(
        "src.service.user.UserService.handle_request", new_callable=AsyncMock
    ) as mock_user_handle, patch(
        "src.config.BodySettings.load",
        return_value={
            "database": "test_db",
            "username": "test_user",
            "password": "test_password",
        },
    ):
        mock_user_handle.side_effect = Exception("Error")

        await startup_event()

        mock_user_handle.assert_called_once()


@pytest.mark.asyncio
async def test_main():
    with patch("uvicorn.Server") as mock_server:
        mock_server_instance = mock_server.return_value
        mock_server_instance.serve = AsyncMock()

        await main()

        mock_server.assert_called_once()
        mock_server_instance.serve.assert_awaited_once()
