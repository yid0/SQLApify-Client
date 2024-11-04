from enum import Enum
from pydantic import (BaseModel, Field, field_validator)
from pydantic_settings import BaseSettings

class SQLApifyBody(BaseModel):
    
    database: str = Field(min_length=3, max_length=20) 
    username: str = Field(min_length=8)
    password: str = Field(min_length=8)
    
    @field_validator("database", "username","password", check_fields=True)
    def validate_not_empty(cls, value):
        if not value:
            raise ValueError(f"Property cannot be empty, given value: {value}")
        return value
   
class SQLApifyBodyEnum(Enum):
    
    APP_DB_NAME=("APP_DB_NAME", "app_db")
    APP_DB_USER=("APP_DB_USER", "app_username") 
    APP_DB_PASSWORD=("APP_DB_PASSWORD", "app_db@Password")
    
    @classmethod
    def load(cls) -> dict: 
        from os import getenv

        cls.env_dict = {
            "provider": "default",
            "database": getenv(str(cls.APP_DB_NAME.value[0])),
            "username": getenv(str(cls.APP_DB_USER.value[0])),
            "password": getenv(str(cls.APP_DB_PASSWORD.value[0])),
        }
        cls.validate(cls.env_dict)
        return cls.env_dict


    @classmethod
    def validate(cls, env_values):
        print("Validator: ", env_values)
        return SQLApifyBody(**env_values)

class BodySettings(BaseSettings, case_sensitive=True):    
    body: dict

    def load(self): 
        try:
            return self.body
        except Exception as e:
            print(f"{e}")
        
    def json(self) -> dict:
        return self.model_dump()["body"]