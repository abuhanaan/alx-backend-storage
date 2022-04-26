#!/usr/bin/env python3
"""lists all documents in a collection
"""

def list_all(mongo_collection):
    """lists all documents in a mongoDB collection
    
    Keyword arguments:
    mongo_collection -- mongoDB collection
    Return: items in the collection
    """
    
    return [doc for doc in mongo_collection.find()]
