from pymongo import *

client = MongoClient()
db = client.test_base
collection = db.test_coll

song = {"Artist": "Macklemore & Ryan Lewis",
        "Song Titel": "Can't Hold Us",
        "Album": "The Heist",
        "Year": 2012
}

test_post = db.posts
post_id = test_post.insert(song)
print test_post.find_one()



