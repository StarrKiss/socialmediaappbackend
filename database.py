import pymongo

import time

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

maindb = myclient["MainDatabase"]myclient = pymongo.MongoClient("mongodb://localhost:27017/")


postcol = maindb["Posts"]

test = {"post": "I love dost", "name": "NAYME!", "time": time.time(), "votes": 0}
mest = {"post": "I hate dost", "name": "gay!", "time": time.time() +20, "votes": 0}

postcol.insert_one(test)
postcol.insert_one(mest)


while True:
    myquery = {"time": {"$lt": time.time()- 20}}
    for x in postcol.find():
        print(x)
    postcol.delete_one(myquery)
