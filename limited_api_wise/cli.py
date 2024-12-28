"""The command line interface to start the application."""

import uvicorn

from limited_api_wise.app import app
from limited_api_wise.settings import Settings


def main():
    """Run the application."""
    uvicorn.run(app, host=Settings.get().host, port=Settings.get().port)


if __name__ == "__main__":
    main()
