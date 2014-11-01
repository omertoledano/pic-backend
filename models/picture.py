from flask import Flask
from flask_mongokit import Document

app = Flask(__name__)


class Picture(Document):
    __collection__ = 'pic'

    structure = {
        'id': long,
        'url': basestring,
        'like_users': [long],
        'dont_like_users': [long]
    }
    required_fields = ['id', 'url']
    default_values = {'like_users': [], 'dont_like_users': []}
    use_dot_notation = True