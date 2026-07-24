# Joe's PIM API

## Overview

This project is a small Product Information Management demonstration built using Python, FastAPI, Uvicorn, SQLModel and SQLite.

The API stores a small number of safety-related products and allows users to retrieve products or add a new product.

## Technologies

* Python
* FastAPI
* Uvicorn
* SQLModel
* SQLite
* Git

## Features

* Creates a local SQLite product database
* Adds sample safety products
* Returns all products
* Returns a specific product by ID
* Adds a new product using a POST request
* Prevents duplicate SKUs
* Logs application activity and API actions
* Provides Swagger API documentation

## Project Structure

```text
pim-api/
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── logging_config.py
│   ├── main.py
│   └── models.py
├── logs/
│   └── .gitkeep
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it in Git Bash:

```bash
source .venv/Scripts/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the API

Run the application using Uvicorn:

```bash
python -m uvicorn app.main:app --reload --port 8001
```

Open the Swagger documentation:

```text
http://127.0.0.1:8001/docs
```

## API Endpoints

| Method | Endpoint                 | Description                 |
| ------ | ------------------------ | --------------------------- |
| GET    | `/`                      | Confirms the API is running |
| GET    | `/products`              | Returns all products        |
| GET    | `/products/{product_id}` | Returns a product by ID     |
| POST   | `/products`              | Adds a new product          |

## Example POST Request

```json
{
  "sku": "PPE-HELMET-001",
  "name": "Industrial Safety Helmet",
  "price": 15.99,
  "stock": 50
}
```

## Logging

The application writes log messages to:

```text
logs/pim_api.log
```

The log records:

* application startup and shutdown
* database creation
* product retrieval
* new product creation
* duplicate product attempts
* missing product requests

The generated log file is excluded from Git because it contains runtime information.
