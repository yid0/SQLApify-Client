from os import getenv
import pytest

pytest_plugins = "pytester"


@pytest.fixture(autouse=True)
def set_env(monkeypatch):
    monkeypatch.setenv("APP_DB_NAME", "test_db")
    monkeypatch.setenv("APP_DB_USER", "test_user")
    monkeypatch.setenv("APP_DB_PASSWORD", "test_password")
    monkeypatch.setenv("SQLAPIFY_ENDPOINT", "http://localhost:8000")
    monkeypatch.setenv("SQLAPIFY_CLIENT_APP_SECRET", "APP_SECRET")

    APP_DB_NAME = getenv("APP_DB_NAME")
    APP_DB_USER = getenv("APP_DB_USER")
    APP_DB_PASSWORD = getenv("APP_DB_PASSWORD")
    SQLAPIFY_ENDPOINT = getenv("SQLAPIFY_ENDPOINT")
    SQLAPIFY_CLIENT_APP_SECRET = getenv("SQLAPIFY_CLIENT_APP_SECRET")

    assert APP_DB_NAME is not None
    assert APP_DB_USER is not None
    assert APP_DB_PASSWORD is not None
    assert SQLAPIFY_ENDPOINT is not None
    assert SQLAPIFY_CLIENT_APP_SECRET is not None
