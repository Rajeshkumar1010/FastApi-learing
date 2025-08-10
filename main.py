from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.get("/")
def read_root():
    return {"message": "Hello, World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def save_item(item_id: int, item: Item):
    return {
        "item_name": item.name,
        "item_price": item.price,
        "is_offer": item.is_offer,
        "item_id": item_id
    }

# POST method with item_id in the URL
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    return {
        "item_name": item.name,
        "item_price": item.price,
        "is_offer": item.is_offer,
        "item_id": item_id
    }
