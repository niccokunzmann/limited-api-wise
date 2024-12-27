"""pytest configuration

You can add responses by running this in your 

See also:
- https://fastapi.tiangolo.com/tutorial/testing/#using-testclient
- 
"""

from typing import Callable, Generator
import pytest
import responses
from pathlib import Path
from fastapi.testclient import TestClient
from limited_api_wise.app import app


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
def rsps():
    """Mock the requests API calls."""
    rsps = responses.RequestsMock()
    rsps.start()
    yield rsps
    rsps.stop(allow_assert=False)


@pytest.fixture
def api() -> Generator[TestClient, None, None]:
    """Return the API test client.
    
    See https://fastapi.tiangolo.com/tutorial/testing/#using-testclient
    """
    return TestClient(app)
    
