#!/usr/bin/env python3
"""Module inserts a new document in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs

    Keyword arguments:
    mongo_collection -- pymongo collection object
    Return: the new_id
    """

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
