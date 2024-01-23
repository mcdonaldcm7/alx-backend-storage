#!/usr/bin/env python3
"""
Task

14. Top students

Write a Python function that returns all students sorted by average score:

    - Prototype: `def top_students(mongo_collection):`
    - `mongo_collection` will be the `pymongo` collection object
    - The top must be ordered
    - The average score must be part of each item returns with key `=
    averageScore
"""
import pymongo


def top_students(mongo_collection):
    """
    Returns all average students sorted by average score
    """
    query = [
            {'$unwind': '$topics'},
            {
                '$group': {
                    '_id': '$_id',
                    'name': {'$first': '$name'},
                    "averageScore": {'$avg': "$topics.score"}
                    }
                },
            {
                '$sort': {
                    "averageScore": -1
                    }
                }
            ]
    students_scores = mongo_collection.aggregate(query)
    return students_scores
