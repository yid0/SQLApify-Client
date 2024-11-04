import pytest
from unittest.mock import patch, AsyncMock
from src.config import BodySettings
from src.service.user import UserService


@pytest.mark.asyncio
async def test_user_service_handle_request():
    body_settings = BodySettings(
        body={
            "database": "test_db",
            "username": "test_user",
            "password": "test_password",
        }
    )

    with patch(
        "src.service.user.Handler.handle", new_callable=AsyncMock
    ) as mock_handle:
        mock_handle.return_value = {"status": "OK"}

        user_service = UserService(body=body_settings)

        response = await user_service.handle_request()

        mock_handle.assert_called_once()

        assert isinstance(response, dict)
        assert str(response) == str({"status": "OK"})
