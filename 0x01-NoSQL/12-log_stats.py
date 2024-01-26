#!/usr/bin/env python3
"""
Task

12. Log stats

Write a Python script that provides some stats about Nginx logs stored in
MongoDB:

    - Database: logs
    - Collection: nginx
    - Display (same as the example):
        * first line: x logs where x is the number of documents in this
        collection
        * second line: Methods:
        * 5 lines with the number of documents with the method = ["GET", "POST"
        , "PUT", "PATCH", "DELETE"] in this order (see example below - warning:
        it’s a tabulation before each line)
        * one line with the number of documents with:
            - method=GET
            - path=/status
"""
import pymongo


if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    logs_collection = client.logs.nginx

    print("{} logs".format(logs_collection.count_documents({})))
    print("Methods:")
    results = list(logs_collection.aggregate([
        {
            "$group": {"_id": "$method", "count": {"$sum": 1}}
        }
    ]))

    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_count = {}

    for r in results:
        if r["_id"] in method:
            method_count[r["_id"]] = r["count"]

    for m in method:
        print("\tmethod ", end='')
        if m in method_count:
            print("{}: {}".format(m, method_count[m]))
        else:
            print("{}: 0".format(m))

    query = [
            {'$match': {"path": "/status"}},
            {'$group': {"_id": "status", 'count': {'$sum': 1}}}
        ]

    status_check = list(logs_collection.aggregate(query))
    if len(status_check) == 0:
        print("0 status check")
    else:
        print("{} status check".format(status_check[0]["count"]))
