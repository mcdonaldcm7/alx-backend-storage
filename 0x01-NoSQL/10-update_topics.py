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


def update_topics(mongo_collection, name, topics):
    """
    Updates school with name `name` topics to `topics`
    """
    mongo_collection.UpdateMany(
            {"name": name},
            {"topics": topics},
            upsert: True
            )
