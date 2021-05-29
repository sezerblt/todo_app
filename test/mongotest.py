from pymongo import MongoClient
import unittest
import pprint

host='mongodb+srv://sezer:mongodB_m13@cluster0.uqiva.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = MongoClient(host)
mydb=client["mydb1"]
mycollection=mydb["todos"]

"""
mypost={
{   "title": "ogle yemegi",
    "description": "oglen yemek yapilacak",
    "is_completed": false,
    "created_date": {
        "$date": "2019-12-31T21:06:00.000Z"
    },
    "updated_date": {
        "$date": "2019-12-30T21:12:00.000Z"
    }
}
}"""

print(mycollection.find_one())
