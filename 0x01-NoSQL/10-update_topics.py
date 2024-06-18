#!/usr/bin/env python3
"""
mod doc
"""


def update_topics(mongo_collection, name, topics):
    """
    func doc
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
