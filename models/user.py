from flask import Flask
from flask_mongokit import Document

app = Flask(__name__)

class User(Document):
    __collection__ = 'user'

    structure = {
        'id': long,
        'username': basestring,
        'like_pics': [long],
        'dont_like_cnt': [long],
        'token': basestring
    }
    required_fields = ['id', 'username']
    default_values = {'like_cnt': [], 'dont_like_cnt': []}
    use_dot_notation = True