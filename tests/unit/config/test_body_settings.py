import pytest
from pydantic import ValidationError
from src.config.body_settings import SQLApifyBodyEnum, BodySettings, SQLApifyBody


def test_sqlapify_body_enum_load(set_env):
    envs = SQLApifyBodyEnum.load()
    assert str(envs) == str(
        {
            "provider": "default",
            "database": "test_db",
            "username": "test_user",
            "password": "test_password",
        }
    )


def test_sqlapify_body_validation_success():
    body = SQLApifyBody(
        database="test_db", username="test_user", password="test_password"
    )
    assert body.database == "test_db"
    assert body.username == "test_user"
    assert body.password == "test_password"


def test_sqlapify_body_validation_failure():
    with pytest.raises(ValidationError) as exeception:
        SQLApifyBody(database="", username="user", password="pass")
    errors = exeception.value.errors()
    assert len(errors) > 0
    assert isinstance(exeception.value, ValidationError)


def test_body_settings_load(set_env):
    envs = SQLApifyBodyEnum.load()
    settings = BodySettings(body=envs)
    settings_dict = settings.json()

    assert isinstance(settings_dict, dict)
    assert str(settings_dict) == str(settings.body)


def test_body_settings_str_representation(set_env):
    envs = SQLApifyBodyEnum.load()
    settings = BodySettings(body=envs)
    settings_dict = settings.json()
    assert isinstance(settings_dict, dict)
    assert str(settings_dict) == str(settings.body)


def test_sqlapify_body_enum_validate_invalid_data():
    with pytest.raises(ValidationError) as exception:
        SQLApifyBodyEnum.validate({"username": "short", "password": "123"})
    error = exception.value
    assert isinstance(error, ValidationError)
