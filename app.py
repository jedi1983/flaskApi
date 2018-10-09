from flask import Blueprint
from flask_restful import Api
from resources.News import News
from resources.Topic import Topic
from resources.Status import Status

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(News, '/News')
api.add_resource(Topic, '/Topic')
api.add_resource(Status, '/Status')