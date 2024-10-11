from pymongo import MongoClient
import os

MONGO_URI = "mongodb+srv://annapareddykrishnateja:teja18@projects.oqkxy.mongodb.net/?retryWrites=true&w=majority&appName=Projects"

client = MongoClient(MONGO_URI)
db = client['fastapi_assignment_db']

client.admin.command('ping')
print("Pinged your deployment. You successfully connected to MongoDB!")

items_collection = db['items']
clockin_collection = db['clock_in']
