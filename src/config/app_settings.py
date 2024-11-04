from pydantic import Field
from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    app_env: str = Field("dev", env="SQLAPIFY_CLIENT_ENV")
    app_name: str = Field("MyApp", env="SQLAPIFY_CLIENT_APP_NAME")
    app_host: str = Field("localhost", env="SQLAPIFY_CLIENT_HOST")
    app_port: int = Field(8000, env="SQLAPIFY_CLIENT_PORT")
    sqlapify_endpoint: str = Field("http://localhost:8000", env="SQLAPIFY_ENDPOINT")
    app_secret: str = Field("defaultsecret", env="SQLAPIFY_CLIENT_APP_SECRET")


    class Config:

        env_file = ".env.dev"
        env_file_encoding = "utf-8"
        case_sensitive = True

