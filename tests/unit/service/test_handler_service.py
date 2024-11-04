import pytest
from unittest.mock import AsyncMock, patch
from src.service.handler import Handler

@pytest.mark.asyncio
async def test_handler_handle():

    method = "GET"
    url = "http://localhost:8000"
    path = "/status"
    body = None

    handler = Handler(method=method, url=url, path=path, body=body)

    mocked_response_data = {"status": "OK"}
    mocked_response = AsyncMock()
    mocked_response.json = AsyncMock(return_value=mocked_response_data)

    with patch("httpx.AsyncClient.build_request") as mock_build_request, \
         patch("httpx.AsyncClient.send", return_value=mocked_response) as mock_send:
        
        response_data = await handler.handle()

        mock_build_request.assert_called_once_with(
            method=method,
            url=f"{url}{path}",
            headers={"caller": "app_secret"},
            json= None
        )

        mock_send.assert_called_once()
        response_data = await mocked_response.json()
        assert isinstance(response_data, dict)
        assert str(response_data) == str(mocked_response_data)
