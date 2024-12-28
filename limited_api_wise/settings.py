"""App configuration.

The settings variable will be used by the app.

T_SETTINGS is the type for the app functions.
See https://fastapi.tiangolo.com/advanced/settings/#read-settings-from-env
"""
import sys
from pydantic_settings import BaseSettings
from typing import Annotated, Literal
from fastapi import Depends
from functools import lru_cache
import pywisetransfer


RUNS_IN_TESTS = "pytest" in sys.modules


class Settings(BaseSettings, cli_parse_args=not RUNS_IN_TESTS):
    """App Settings
    
    See https://fastapi.tiangolo.com/advanced/settings/#run-the-server
    
    wise_environment - Environment to connect to. Available: sandbox, live
    If you make modifications, you will need to change the source_code_url.
    """
    environment : Literal["live", "sandbox"] = "sandbox"
    api_token : str = "00000000-0000-0000-0000-000000000000"
    host : str = "0.0.0.0"
    port : int = 8000
    source_code_url : str = "https://github.com/niccokunzmann/limited-api-wise"

    @staticmethod
    @lru_cache
    def get() -> "Settings":
        """Get the settings singleton."""
        return Settings()

    @property
    def client(self) -> pywisetransfer.Client:
        return pywisetransfer.Client(environment=self.environment, api_token=self.api_token)


SETTINGS = Annotated[Settings, Depends(Settings.get)]

__all__ = ["Settings", "SETTINGS"]
