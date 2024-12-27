"""App configuration.

The settings variable will be used by the app.
"""
from pydantic_settings import BaseSettings
from typing import Literal


class Settings(BaseSettings, cli_parse_args=True):
    """App Settings
    
    See https://fastapi.tiangolo.com/advanced/settings/#run-the-server
    
    wise_environment - Environment to connect to. Available: sandbox, live
    """
    wise_environment : Literal["live", "sandbox"] = "sandbox"
    host : str = "0.0.0.0"
    port : int = 8000


settings = Settings()

__all__ = ["settings", "Settings"]
