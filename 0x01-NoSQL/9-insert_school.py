#!/usr/bin/env python3
"""
Task

9. Insert a document in Python

Write a Python function that inserts a new document in a collection based on
`kwargs`:

    - Prototype: `def insert_school(mongo_collection, **kwargs):`
    - `mongo_collection` will be the `pymongo` collection object
    - Returns the new `_id`
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Returns the new `_id` for the inserted documen
    """
    return mongo_collection.insert_one(kwargs)
