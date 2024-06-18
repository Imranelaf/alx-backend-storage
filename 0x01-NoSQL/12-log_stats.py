#!/usr/bin/env python3

'''
This script will query the logs collection in the nginx database and print out
the number of logs, the number of logs for each HTTP method, and the number of
logs for the /status path.
'''

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017')
    collection = client.logs.nginx

    print("{} logs".format(collection.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for m in methods:
        print(
            f'\tmethod {m}: {collection.count_documents({"method": m})}'
            )
    print(f"{collection.count_documents({'path': '/status'})} status check")
