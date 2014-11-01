from flask import Flask
from flask_mongokit import Document

app = Flask(__name__)

class User(Document):
    __collection__ = 'user'

    structure = {
        'fb_user_id': basestring,
        'user_token': basestring,
        'like_pics': [long],
        'dont_like_pics': [long]
    }
    required_fields = ['fb_user_id', 'user_token']
    default_values = {'like_pics': [], 'dont_like_pics': []}
    use_dot_notation = True