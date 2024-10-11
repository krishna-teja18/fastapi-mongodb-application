# FastAPI CRUD Application with MongoDB

This is a FastAPI application that provides CRUD operations on **Items** and **User Clock-In Records** with MongoDB as the backend. It also includes filtering and aggregation functionalities.

## Features

- CRUD operations for items.
- CRUD operations for clock-in records.
- Filtering and aggregation support.
- Swagger documentation for easy testing.

## Project Setup

### Prerequisites

- Python 3.7+
- MongoDB (cloud or local instance)

### Steps to Set Up the Project Locally

1. Clone the repository:

```
git clone https://github.com/krishna-teja18/fastapi-mongodb-application.git
```

2. Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Update the MongoDB connection string in `database.py`:

```
client = MongoClient("your-mongodb-connection-string")
```

5. Run the FastAPI app using Uvicorn:

```
uvicorn app.main:app --reload
```

6. Access Swagger documentation at:

```
http://127.0.0.1:8000/docs
```

## Endpoints

### Items API

1. POST /items: Create a new item.
2. GET /items/{item_id}: Retrieve a specific item.
3. GET /items/filter: Filter items based on email, expiry date, insert date, and quantity.
4. PUT /items/{item_id}: Update an item by ID.
5. DELETE /items/{item_id}: Delete an item by ID.
6. GET /items/aggregate: Get aggregated item data based on emails.

### Clock-In API
1. POST /clock-in: Create a new clock-in record.
2. GET /clock-in/{id}: Retrieve a specific clock-in record.
3. GET /clock-in/filter: Filter clock-in records by email, location, and insert date.
4. PUT /clock-in/{id}: Update a clock-in record by ID.
5. DELETE /clock-in/{id}: Delete a clock-in record by ID.

