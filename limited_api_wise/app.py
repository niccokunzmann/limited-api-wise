from fastapi import FastAPI
from .settings import SETTINGS


app = FastAPI()


@app.get("/settings.json")
@app.get("/v1/settings")
def read_main(settings: SETTINGS):
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


@app.get("/v1/accounts")
def get_sub_accounts():
    """Get a list of all the sub-accounts."""


__all__ = ["app"]
