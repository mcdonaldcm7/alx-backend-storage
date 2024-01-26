#!/usr/bin/env python3
"""
Task

15. Log stats - new version

Improve 12-log_stats.py by adding the top 10 of the most present IPs in the
collection nginx of the database logs:

    - The IPs top must be sorted
"""
import pymongo


if __name__ == "__main__":
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    print('{} logs'.format(logs_collection.count_documents({})))
    print('Methods:')
    results = list(logs_collection.aggregate([
        {
            '$group': {'_id': "$method", 'count': {"$sum": 1}}
        }
    ]))

    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_count = {}

    for r in results:
        if r["_id"] in method:
            method_count[r["_id"]] = r["count"]

    for m in method:
        print("\tmethod ", end="")
        if m in method_count:
            print("{}: {}".format(m, method_count[m]))
        else:
            print("{}: 0".format(m))

    status_query = [
            {'$match': {"path": "/status"}},
            {'$group': {"_id": "status", 'count': {'$sum': 1}}}
        ]

    status_check = list(logs_collection.aggregate(status_query))
    if len(status_check) == 0:
        print("0 status check")
    else:
        print("{} status check".format(status_check[0]["count"]))

    ip_query = [
            {
                '$group': {
                    "_id": "$ip",
                    "count": {'$sum': 1}
                    }
                },
            {
                '$sort': {
                    'count': -1
                    }
                },
            {'$limit': 10}
        ]
    ip_freq = list(logs_collection.aggregate(ip_query))
    print("IPs:")
    for ip in ip_freq:
        print('\t{}: {}'.format(ip['_id'], ip['count']))
