"""
Main application module for the FastAPI CRUD application.

This module defines the API endpoints for the application.
"""

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """
    Handle GET requests to the root path.
    
    Returns:
        dict: A simple greeting message.
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    """
    Handle GET requests to retrieve an item by ID.
    
    Args:
        item_id (int): The ID of the item to retrieve.
        q (Union[str, None], optional): An optional query parameter. Defaults to None.
        
    Returns:
        dict: A dictionary containing the item ID and query parameter.
    """
    return {"item_id": item_id, "q": q}
