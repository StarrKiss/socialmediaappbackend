import pymongo

import time

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

maindb = myclient["MainDatabase"]myclient = pymongo.MongoClient("mongodb://localhost:27017/")


postcol = maindb["Posts"]


while True:
    myquery = {"time": {"$lt": time.time()- 600}}
    for x in postcol.find():
        print(x)
    postcol.delete_one(myquery)
