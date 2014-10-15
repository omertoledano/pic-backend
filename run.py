from eve import Eve
from flask import jsonify

app = Eve()


@app.route("/images/random")
def get_random_image():
    return jsonify({'url': 'http://www.imgion.com/images/01/beautiful-village-home.jpg'})


if __name__ == '__main__':
    app.run()