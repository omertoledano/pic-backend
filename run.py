from eve import Eve
from flask import jsonify
from flask_cors import CORS

app = Eve()
cors = CORS(app, resources={r'/api/v1/*': {"origins": "*"}})

@app.route("/api/v1/images/random")
def get_random_image():
    return jsonify({'url': 'http://www.imgion.com/images/01/beautiful-village-home.jpg'})


if __name__ == '__main__':
    app.run()