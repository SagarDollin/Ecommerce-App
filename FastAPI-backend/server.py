from Authentication.login import get_current_active_user, get_current_user, User
from server_app import app
from typing import Union

from fastapi import Depends, FastAPI
from fastapi.security.api_key import APIKey
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
import uvicorn

from Microservices.wallet import spend, add
from Microservices.products import search
from Authentication.login import *
from starlette.responses import  JSONResponse

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/secure_endpoint", tags=["test"])
async def get_open_api_endpoint(current_user: User = Depends(get_current_active_user)):
    response = "How cool is this?"
    return response

if __name__ == "__main__":
    uvicorn.run("server:app", port=8004)


