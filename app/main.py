# main.py

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/post-req")
async def read_root(data):
    print(data)
    return {"Hello": "world"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)