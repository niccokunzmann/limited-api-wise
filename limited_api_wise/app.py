from fastapi import FastAPI
from .settings import SETTINGS


app = FastAPI()

@app.get("/settings.json")
def read_main(settings:SETTINGS):
    from .version import __version__, __version_tuple__
    return {
        "license": "AGPL-3.0",
        "environment": settings.environment,
        "version": {
            "source": settings.source_code_url,
            "text": __version__,
            "list": __version_tuple__,
        },
    }

__all__ = ["app"]
