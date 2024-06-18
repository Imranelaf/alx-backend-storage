#!/usr/bin/env python3
"""
mod doc
"""


def insert_school(mongo_collection, **kwargs):
    """
    func doc
    """
    return mongo_collection.insert_one(kwargs).inserted_id
