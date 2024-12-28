"""App configuration.

The settings variable will be used by the app.

T_SETTINGS is the type for the app functions.
"""
from pydantic_settings import BaseSettings
from typing import Annotated, Literal
from fastapi import Depends
from functools import lru_cache


class Settings(BaseSettings, cli_parse_args=True):
    """App Settings
    
    See https://fastapi.tiangolo.com/advanced/settings/#run-the-server
    
    wise_environment - Environment to connect to. Available: sandbox, live
    """
    environment : Literal["live", "sandbox"] = "sandbox"
    host : str = "0.0.0.0"
    port : int = 8000

    @staticmethod
    @lru_cache
    def get() -> "Settings":
        """Get the settings singleton."""
        return Settings()


T_SETTINGS = Annotated[Settings, Depends(Settings.get)]

__all__ = ["Settings", "T_SETTINGS"]
