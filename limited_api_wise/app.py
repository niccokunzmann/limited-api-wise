from fastapi import FastAPI
import pywisetransfer
from . import settings


app = FastAPI()

@app.get("/")
def read_main():
    return {"msg": "Hello World"}


__all__ = ["app"]
