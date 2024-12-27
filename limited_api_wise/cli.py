"""The command line interface to start the application."""
import uvicorn

from limited_api_wise.app import app
from limited_api_wise.settings import settings

def main():
    """Run the application."""
    uvicorn.run(app, host=settings.host, port=settings.port)

if __name__ == "__main__":
    main()
