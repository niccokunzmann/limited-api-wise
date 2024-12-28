"""pytest configuration

You can add responses by running this in your 

See also:
- https://fastapi.tiangolo.com/tutorial/testing/#using-testclient
- 
"""

from datetime import datetime
from typing import Callable, Generator
import pytest
from responses import RequestsMock
from pathlib import Path
from fastapi.testclient import TestClient
from limited_api_wise.app import app
from limited_api_wise import settings
from limited_api_wise.wise import Wise
from iso4217 import Currency
from munch import Munch, munchify


HERE = Path(__file__).parent
RESPONSES_WISE = HERE / "wise"


for file in RESPONSES_WISE.iterdir():
    # Read all the YAML files and create fixtures.
    if file.suffix.lower() in (".yaml", ".yml"):

        @pytest.fixture(name=file.stem)
        def api_to_load(rsps, file_path=file):
            """Load a specific API."""
            rsps._add_from_file(file_path)
            return rsps


@pytest.fixture
def rsps() -> Generator[RequestsMock, None, None]:
    """Mock the requests API calls."""
    rsps = RequestsMock()
    rsps.start()
    yield rsps
    rsps.stop(allow_assert=False)


@pytest.fixture
def api() -> Generator[TestClient, None, None]:
    """Return the API test client.

    See https://fastapi.tiangolo.com/tutorial/testing/#using-testclient
    """
    return TestClient(app)


@pytest.fixture
def settings() -> Generator[settings.Settings, None, None]:
    """Return the app settings."""
    old_settings = settings.settings.model_copy()
    yield settings.settings
    settings.settings = old_settings


class MockWiseClient:
    """Mock the requests to the wise API."""

    def __init__(self):
        self._transfers = []
        self.transfers = self

    def add_standard(
        self, target: Currency, amount: int, reference: str, source: Currency = Currency.EUR, status:str="outgoing_payment_sent"
    ):
        """Add a transfer."""

        self._transfers.append(
            {
                "id": 43726374 + len(self._transfers),
                "user": 1124124,
                "targetAccount": 63748,
                "sourceAccount": None,
                "quote": 657171,
                "status": "outgoing_payment_sent",
                "reference": reference,
                "rate": 0.89,
                "created": "2017-11-24 10:47:{:02d}".format(len(self._transfers)),
                "business": None,
                "transferRequest": None,
                "details": {"reference": reference},
                "hasActiveIssues": None,
                "sourceCurrency": str(source),
                "sourceValue": 0,
                "targetCurrency": str(target),
                "targetValue": amount,
                "customerTransactionId": "54a6bc09-cef9-49a8-9041-f1f0c654cd{:02d}".format(
                    len(self._transfers)
                ),
            }
        )

    def list(self, profile_id: int, offset: int=None, limit: int=None) -> list[Munch]:
        """List the transfers"""
        assert offset % limit == 0
        return [munchify(t) for t in self._transfers[offset : offset + limit]]


@pytest.fixture
def transfers() -> MockWiseClient:
    """The transfers we make."""


@pytest.fixture
def wise(transfers) -> Wise:
    return Wise(transfers)
