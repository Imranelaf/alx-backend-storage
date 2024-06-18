#!/usr/bin/env python3

'''
This script will query the logs collection in the logs database to
display the number of documents in the collection, the number of
documents with a specific field value, and the number of documents
'''

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017')
    clc = client.logs.nginx

    print("{} logs".format(clc.count_documents({})))
    print("Methods:")
    ms = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for m in ms:
        print("\tmethod {}: {}".format(m, clc.count_documents({"method": m})))
    print("{} status check".format(
        clc.count_documents({"path": "/status"})))

    print("IPs:")
    ips = clc.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in ips:
        print("\t{}: {}".format(ip.get("_id"), ip.get("count")))
