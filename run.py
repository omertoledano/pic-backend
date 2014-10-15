import json
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


@app.route("/test")
def test():
    try:
        print db.Picture.find()
    except Exception as e:
        print e



@app.route("/api/v1/images/random")
def get_random_image():
    return jsonify({'url': 'http://www.imgion.com/images/01/beautiful-village-home.jpg', 'id': 1})


@app.route("/api/v1/image/<int:image_id>/like", methods=['POST'])
def save_op(image_id):
    print image_id, json.loads(request.data)['op']
    return jsonify({})


if __name__ == '__main__':
    app.run()