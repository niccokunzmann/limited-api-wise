"""App configuration.

The settings variable will be used by the app.

T_SETTINGS is the type for the app functions.
See https://fastapi.tiangolo.com/advanced/settings/#read-settings-from-env
"""

import sys
from pydantic_settings import BaseSettings
from typing import Annotated, Literal, Optional
from fastapi import Depends
from functools import lru_cache
import pywisetransfer

from limited_api_wise.wise import Wise


RUNS_IN_TESTS = "pytest" in sys.modules


class Settings(BaseSettings, cli_parse_args=not RUNS_IN_TESTS):
    """App Settings

    See https://fastapi.tiangolo.com/advanced/settings/#run-the-server

    wise_environment - Environment to connect to. Available: sandbox, live
    If you make modifications, you will need to change the source_code_url.
    """

    environment: Literal["live", "sandbox"] = "sandbox"
    api_token: str = "6f2cb1c1-2d29-41a7-a8f1-b47c1aca73e8"
    host: str = "0.0.0.0"
    port: int = 8000
    profile_id: int = 28582534
    source_code_url: str = "https://github.com/niccokunzmann/limited-api-wise"

    @staticmethod
    @lru_cache
    def get() -> "Settings":
        """Get the settings singleton."""
        return Settings()

    @property
    def client(self) -> pywisetransfer.Client:
        return pywisetransfer.Client(self.api_token, environment=self.environment)

    @property
    def wise(self) -> Wise:
        return Wise(self.client, self.profile_id)


SETTINGS = Annotated[Settings, Depends(Settings.get)]


def _get_wise() -> Wise:
    return Settings.get().wise


WISE = Annotated[Wise, Depends(_get_wise)]

__all__ = ["Settings", "SETTINGS", "WISE"]
