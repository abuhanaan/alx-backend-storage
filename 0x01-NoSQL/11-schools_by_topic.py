#!/usr/bin/env python3
"""Module returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic

    Keyword arguments:
    mongo_collection -- pymongo collection object
    topic -- topic searched
    Return: list of schools with specified topics
    """

    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
