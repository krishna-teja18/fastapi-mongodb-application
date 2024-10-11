from fastapi import FastAPI, HTTPException, status
from .schemas import ItemCreateSchema, ItemUpdateSchema, ClockInCreateSchema, ClockInUpdateSchema
from .crud import *
from bson import ObjectId

app = FastAPI()

# Items API

@app.post("/items", status_code=status.HTTP_201_CREATED)
async def create_item_api(item: ItemCreateSchema):
    item_data = item.dict()
    create_item(item_data)
    return {"message": "Item created successfully"}

@app.get("/items/aggregate")
async def aggregate_items():
    aggregation_result = aggregate_items_by_email()
    return aggregation_result

@app.get("/items/filter")
async def filter_items(email: str = None, expiry_date: str = None, insert_date: str = None, quantity: int = None):
    try:
        filter_query = {}
        if email:
            filter_query['email'] = email
        if expiry_date:
            filter_query['expiry_date'] = {"$gt": expiry_date}
        if insert_date:
            filter_query['insert_date'] = {"$gt": insert_date}
        if quantity:
            filter_query['quantity'] = {"$gte": quantity}

        items = get_items_by_filter(filter_query)

        if not items:
            raise HTTPException(status_code=404, detail="Items not found")

        return items

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=400, detail="Invalid query parameters or server error")

@app.get("/items/{item_id}")
async def get_item_api(item_id: str):
    try:
        obj_id = ObjectId(item_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ObjectId format")
    
    item = get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item 

@app.put("/items/{item_id}")
async def update_item_api(item_id: str, item_update: ItemUpdateSchema):
    update_data = item_update.dict(exclude_unset=True)
    result = update_item(item_id, update_data)
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item updated successfully"}

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item_api(item_id: str):
    result = delete_item(item_id)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")

# Clock-in Records API

@app.post("/clock-in", status_code=status.HTTP_201_CREATED)
async def create_clockin_api(clockin: ClockInCreateSchema):
    clockin_data = clockin.dict()
    create_clockin(clockin_data)
    return {"message": "Clock-in created successfully"}

@app.get("/clock-in/filter")
async def filter_clockins(email: str = None, location: str = None, insert_datetime: str = None):
    filter_query = {}
    if email:
        filter_query['email'] = email
    if location:
        filter_query['location'] = location
    if insert_datetime:
        filter_query['insert_datetime'] = {"$gt": insert_datetime}

    clockins = get_clockins_by_filter(filter_query)
    return clockins

@app.get("/clock-in/{clockin_id}")
async def get_clockin_api(clockin_id: str):
    try:
        obj_id = ObjectId(clockin_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ObjectId format")
    
    clockin = get_clockin(clockin_id)
    if not clockin:
        raise HTTPException(status_code=404, detail="Item not found")
    return clockin

@app.put("/clock-in/{clockin_id}")
async def update_clockin_api(clockin_id: str, clockin_update: ClockInUpdateSchema):
    update_data = clockin_update.dict(exclude_unset=True)
    result = update_clockin(clockin_id, update_data)
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    return {"message": "Clock-in updated successfully"}

@app.delete("/clock-in/{clockin_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_clockin_api(clockin_id: str):
    result = delete_clockin(clockin_id)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
