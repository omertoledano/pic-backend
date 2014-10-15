from flask import Flask
from flask_mongokit import Document, MongoKit

app = Flask(__name__)


class Picture(Document):
    __collection__ = 'pic'

    structure = {
        'id': long,
        'url': basestring,
        'like_cnt': int,
        'dont_like_cnt': int
    }
    required_fields = ['id', 'url']
    default_values = {'like_cnt': 0, 'dont_like_cnt': 0}
    use_dot_notation = True