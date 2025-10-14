#
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
def get_items():
    return{"item_1","item_2","item_3"}

@app.post("/items/{items}")
def items(items: str, price: float):
    return{"name":items,"price": price}