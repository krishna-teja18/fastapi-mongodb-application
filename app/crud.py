from pymongo.errors import DuplicateKeyError
from bson import ObjectId
from .database import items_collection, clockin_collection
from datetime import datetime

# CRUD operations for Items
def create_item(item_data):
    item_data["insert_date"] = datetime.utcnow()
    return items_collection.insert_one(item_data)

def get_item(item_id):
    # print(item_id)
    item = items_collection.find_one({"_id": ObjectId(item_id)})
    if item:
        item["_id"] = str(item["_id"])
    return item

def get_items_by_filter(filter_data):
    items = list(items_collection.find(filter_data))
    for item in items:
        item["_id"] = str(item["_id"])
    return items

def aggregate_items_by_email():
    return list(items_collection.aggregate([
        {"$group": {"_id": "$email", "count": {"$sum": 1}}}
    ]))

def update_item(item_id, updated_data):
    return items_collection.update_one({"_id": ObjectId(item_id)}, {"$set": updated_data})

def delete_item(item_id):
    return items_collection.delete_one({"_id": ObjectId(item_id)})

# CRUD operations for Clock-in Records
def create_clockin(clockin_data):
    clockin_data["insert_datetime"] = datetime.utcnow()
    return clockin_collection.insert_one(clockin_data)

def get_clockin(clockin_id):
    clockin = clockin_collection.find_one({"_id": ObjectId(clockin_id)})
    if clockin_id:
        clockin["_id"] = str(clockin["_id"])
    return clockin

def get_clockins_by_filter(filter_data):
    clockins = list(clockin_collection.find(filter_data))
    for clockin in clockins:
        clockin["_id"] = str(clockin["_id"])
    return clockins

def update_clockin(clockin_id, updated_data):
    return clockin_collection.update_one({"_id": ObjectId(clockin_id)}, {"$set": updated_data})

def delete_clockin(clockin_id):
    return clockin_collection.delete_one({"_id": ObjectId(clockin_id)})
