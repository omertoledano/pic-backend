import json
from random import randint

from flask import jsonify, request, Flask, abort
from flask_cors import CORS
from flask_mongokit import MongoKit
from models.picture import Picture


app = Flask(__name__)
app.config.from_object('settings')
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r'/api/v1/*': {"origins": "*"}})
db = MongoKit(app)
db.register([Picture])


@app.route("/api/v1/fb_user_token", methods=['POST'])
def get_user_token():
    fb_id = request.args.get('fb_user_id')
    print fb_id
    return jsonify({"token": "111"})


@app.route("/api/v1/images/random")
def get_random_image():
    res = list(db.Picture.find())
    rand_int = randint(0, len(res))
    d = {'id': res[rand_int].id, 'url': res[rand_int].url}
    return jsonify(d)


@app.route("/api/v1/image/<int:image_id>/like", methods=['POST'])
def save_op(image_id):
    try:
        request_data = json.loads(request.data)
        print image_id, request_data['op']
        update_dict = build_update_dict(json.loads(request.data)['op'], request_data['user_token'])
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