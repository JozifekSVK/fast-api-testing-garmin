# main.py

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    activities: list

@app.post("/post-req/")
async def create_user(user_data: UserCreate):
    for element in user_data.activities:
        print(element)

    print(user_data)
    return {
        "msg": "we got data succesfully"
    }

@app.get("/")
async def read_root():
    return {"Hello": "World, new version"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)