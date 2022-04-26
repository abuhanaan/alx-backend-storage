#!/usr/bin/env python3
""" Module returns all students sorted by average score
    The top must be ordered
    The average score must be part of each item returns with key = averageScore
"""


def top_students(mongo_collection):
    """Prints all students in a collection accordng to their average score.

    Keyword arguments:
    mongo_collection -- pymongo collection object
    Return: students
    """

    students = mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score',
                        },
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1},
            },
        ]
    )
    return students
