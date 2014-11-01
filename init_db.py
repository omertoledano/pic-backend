from flask import Flask
from flask_mongokit import MongoKit
from flask_pymongo.wrappers import MongoClient
from settings import MONGODB_HOST, MONGODB_PORT, MONGODB_DATABASE
from models.picture import Picture

MIN_HASH_RESULT = -(2**32)
MONGODB_COLLECTION_NAME = 'pic'

pics = [
    {'url': 'http://www.thetimes.co.uk/tto/multimedia/archive/00309/108787995_309592c.jpg',
     'like_users': [], 'dont_like_users': []},
    {'url': 'http://cdni.wired.co.uk/620x413/s_v/shutterstock_65735200.jpg',
     'like_users': [], 'dont_like_users': []},
    {'url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4ufFVwmoe1ltmoJstyx8OS23hf6g9HlPzYY-QVAhlx5q-CzRy',
     'like_users': [], 'dont_like_users': []}
]

app = Flask(__name__)
app.config.from_object('settings')
db = MongoKit(app)
db.register([Picture])

def drop_and_init():
    c = MongoClient(MONGODB_HOST, MONGODB_PORT)
    drop(c, MONGODB_DATABASE)
    init(MONGODB_COLLECTION_NAME)


def drop(client, db_name):
    client.drop_database(db_name)


def init(collection_name):
    with app.app_context():
        col = db[collection_name]
        for pic in pics:
            new_id = hash(pic['url']) - MIN_HASH_RESULT
            pic['id'] = new_id
            insert_to_db(col, pic)


def insert_to_db(collection, pic):
    modeled_pic = collection.Picture()
    for key, value in pic.iteritems():
        modeled_pic[key] = value
    modeled_pic.save()


if __name__ == '__main__':
    drop_and_init()