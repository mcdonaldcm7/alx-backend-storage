#!/usr/bin/env python3
"""
Task

10. Change school topics

Write a Python function that changes all topics of a school document based on
the name:

    - Prototype: `def update_topics(mongo_collection, name, topics):`
    - `mongo_collection` will be the `pymongo` collection object
    - `name` (string) will be the school name to update
    - `topics` (list of strings) will be the list of topics approached in the
    school
"""
import pymongo
from typing import List


def update_topics(mongo_collection: pymongo.Collection, name: str,
                  topics: List[str]):
    """
    Updates school with name `name` topics to `topics`
    """
    _id = mongo_collection.update_many({"name": name},
                                       {"$set": {"topics": topics}},
                                       upsert=True
                                       )
    return (_id.upserted_id)
