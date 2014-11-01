import json
from random import randint
import uuid

from flask import jsonify, request, Flask, abort
from flask_cors import CORS
from flask_mongokit import MongoKit
from models.picture import Picture
from models.user import User


app = Flask(__name__)
app.config.from_object('settings')
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r'/api/v1/*': {"origins": "*"}})
db = MongoKit(app)
db.register([Picture, User])


@app.route("/api/v1/fb_user_id", methods=['POST'])
def get_user_token():
    try:
        fb_id = get_request_form()['fb_user_id']
        print fb_id
        user = get_user(fb_id)
    except Exception as e:
        print e
    return jsonify({"user_token": user['user_token']})


def get_request_form():
    if len(request.form) > 0:
        return request.form
    return request.data


def get_request_args():
    if len(request.args) > 0:
        return request.args
    return request.data


def get_user(fb_id):
    user = db.User.find_one({'fb_user_id': fb_id})
    if user is not None:
        return user
    user = db.User()
    user['fb_user_id'] = fb_id
    user['user_token'] = str(uuid.uuid4())
    user.save()
    return user


@app.route("/api/v1/images/random")
def get_random_image():
    res = list(db.Picture.find())
    rand_int = randint(0, len(res))
    d = {'id': res[rand_int].id, 'url': res[rand_int].url}
    return jsonify(d)


@app.route("/api/v1/image/<int:image_id>/like", methods=['POST'])
def save_op(image_id):
    try:
        request_form = json.loads(get_request_form())
        print image_id, request_form['op']
        update_dict = build_update_dict(request_form['op'], request_form['user_token'])
        db[Picture.__collection__].update({'id': image_id}, update_dict, False)
    except Exception as e:
        print e
    return jsonify({})


def build_update_dict(op, user_token):
    if user_token is None:
        return
    if op == 'like':
        return {'$addToSet': {'like_users': user_token}}
    elif op == 'dont_like':
        return {'$addToSet': {'dont_like_users': user_token}}
    abort(404)


if __name__ == '__main__':
    app.run()