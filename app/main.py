# main.py

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    user_id: int
    username: str

@app.post("/post-req/")
async def create_user(user_data: UserCreate):
    user_id = user_data.user_id
    username = user_data.username

    print(user_id)
    print(username)
    return {
        "msg": "we got data succesfully",
        "user_id": user_id,
        "username": username,
    }

@app.get("/")
async def read_root():
    return {"Hello": "World, new version"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)