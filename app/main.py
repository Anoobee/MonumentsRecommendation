# main.py
import os
from fastapi import FastAPI
from typing import Optional
from typing import List
import json
import asyncio
from .recommend import recommend_monuments

app = FastAPI()


@app.get("/say_hello")
async def read_item():
    return {"message": "Hello World"}


@app.post("/getRecommendations")
async def get_recommendations(prompt: Optional[str] = None):
    return recommend_monuments()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
