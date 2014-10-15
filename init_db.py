import sys
from flask_pymongo.wrappers import MongoClient
from settings import MONGO_DBNAME, MONGO_HOST, MONGO_PORT, MONGO_COLLECTION_NAME

MIN_HASH_RESULT = -(2**32)

pics = [
    {'url': 'http://www.thetimes.co.uk/tto/multimedia/archive/00309/108787995_309592c.jpg',
     'like_cnt': 0, 'dont_like_cnt': 0},
    {'url': 'http://cdni.wired.co.uk/620x413/s_v/shutterstock_65735200.jpg',
     'like_cnt': 0, 'dont_like_cnt': 0},
    {'url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4ufFVwmoe1ltmoJstyx8OS23hf6g9HlPzYY-QVAhlx5q-CzRy',
     'like_cnt': 0, 'dont_like_cnt': 0}
]


def drop_and_init():
    c = MongoClient(MONGO_HOST, MONGO_PORT)
    drop(c, MONGO_DBNAME)
    init(c, MONGO_DBNAME, MONGO_COLLECTION_NAME)


def drop(client, db_name):
    client.drop_database(db_name)


def init(client, db_name, collection_name):
    db = client[db_name]
    col = db[collection_name]
    for pic in pics:
        new_id = hash(pic['url']) - MIN_HASH_RESULT
        pic['id'] = new_id
        col.insert(pic)

if __name__ == '__main__':
    drop_and_init()