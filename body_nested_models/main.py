from typing import Dict, List, Optional, Set

from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.networks import HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str

    class Config:
        schema_extra = {
            "example": {"url": "http://example.org/image.jpg", "name": "Name"}
        }


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    image: Optional[List[Image]] = None


class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: List[Item]


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer


@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images


@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights
