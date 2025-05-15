# main.py
import os
from fastapi import FastAPI, Form
from typing import Optional
from typing import List, Literal
import json
import asyncio
from .recommend import recommend_monuments

app = FastAPI()


@app.get("/say_hello")
async def read_item():
    return {"message": "Hello World"}


@app.post("/getRecommendations")
async def get_recommendations(
    latitude: float = Form(..., description="Latitude of your location"),
    longitude: float = Form(..., description="Longitude of your location"),
    preferred_type: Literal[
        "Hindu Temple",
        "Buddhist Temple",
        "Historical Monument",
        "Garden",
        "Historical Site",
        "Museum",
        "Park",
        "Cave",
    ] = Form(..., description="Your preferred type of monument"),
):
    # Pass the parameters to the recommend_monuments function
    return recommend_monuments(latitude, longitude, str(preferred_type))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
