import pytest
from unittest.mock import patch, AsyncMock
from src.service.status import StatusService
from src.service.handler import Handler


@pytest.mark.asyncio
async def test_handle_request():
    with patch.object(Handler, "handle", new_callable=AsyncMock) as mock_handle:
        mock_handle.return_value = {"status": "OK"}

        status_service = StatusService()
        response = await status_service.handle_request()
        assert isinstance(response, dict)
        assert response == {"status": "OK"}
        mock_handle.assert_awaited_once()
