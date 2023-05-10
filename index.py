from typing import Union

import random as rd
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

items = {
    "1": {"name": "Foo", "price": 50.2},
    "2": {"name": "Bar", "price": 62},
    "3": {"name": "Baz", "price": 50.8},
    "4": {"name": "Too", "price": 54.3},
    "5": {"name": "Boo", "price": 20.6},
}


personalInfo = {
    "Name": "Hasnain Habib Sayed",
    "Age" : "23",
    "Contact" : "01800000000"
}

# endpoint in postman: http://localhost:5000/item
@app.get("/item")
async def read_item():
    random_key = rd.choice(list(items.keys())) ## randomly selecting a key in items
    random_value = items[random_key]  ## calling the value of the selected key
    return {"message": random_value}  ## returning the value

# endpoint in postman: http://localhost:5000/items
@app.get("/items")
async def read_items():
    return items     ## returning all the value


# endpoint in postman: http://localhost:5000/personal_info
@app.get("/personal_info")
async def read_personal_info():
    return personalInfo     ## returning personal info

# start the app → uvicorn index:app --port 5000 --reload --log-level debug