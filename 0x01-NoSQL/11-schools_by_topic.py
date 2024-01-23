#!/usr/bin/env python3
"""
Task

11. Where can I learn Python?

Write a Python function that returns the list of school having a specific
topic:

    - Prototype: `def schools_by_topic(mongo_collection, topic):`
    - `mongo_collection` will be the `pymongo` collection object
    - `topic` (string) will be topic searched
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Return the list of school having a specific topic
    """
    query = {"topics": {"$elemMatch": {"eq": topic}}}
    return mongo_collection.find(query)
