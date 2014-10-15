import json
from random import randint

from flask import jsonify, request, Flask
from flask_cors import CORS
from flask_mongokit import MongoKit
from models.picture import Picture


app = Flask(__name__)
app.config.from_object('settings')
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r'/api/v1/*': {"origins": "*"}})
db = MongoKit(app)
db.register([Picture])


@app.route("/api/v1/images/random")
def get_random_image():
    res = list(db.Picture.find())
    rand_int = randint(0, len(res))
    d = {'id': res[rand_int].id, 'url': res[rand_int].url}
    return jsonify(d)



@app.route("/api/v1/image/<int:image_id>/like", methods=['POST'])
def save_op(image_id):
    print image_id, json.loads(request.data)['op']
    return jsonify({})


if __name__ == '__main__':
    app.run()