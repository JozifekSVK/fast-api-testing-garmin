# main.py

from requests import post
import uvicorn
import requests
from fastapi import FastAPI
from pydantic import BaseModel
import logging
from threading import Thread
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()

class UserCreate(BaseModel):
    activities: list

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
	exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
	logging.error(f"{request}: {exc_str}")
	content = {'status_code': 10422, 'message': exc_str, 'data': None}
	return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

@app.post("/post-req/")
async def create_user(request_data: dict) -> dict:

    url = 'http://147.175.144.168:8181/fit-file'
    
    Thread(target=post, args=(url,), kwargs={'json': request_data}).start()

    return {
        "msg": "we got data succesfully"
    }

@app.get("/")
async def read_root():
    return {"Hello": "World, new version"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
