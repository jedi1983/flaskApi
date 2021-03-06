from flask import Blueprint
from flask_restful import Api
from resources.News import News
from resources.Topic import Topic
from resources.Status import Status
from resources.TopicNews import TopicNews
from resources.NewsByTopic import NewsByTopic
from resources.NewsByStatus import NewsByStatus

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(News, '/News')
api.add_resource(Topic, '/Topic')
api.add_resource(Status, '/Status')
api.add_resource(TopicNews, '/TopicNews')
api.add_resource(NewsByTopic,'/News/<string:topic>',endpoint='News')
api.add_resource(NewsByStatus,'/News/Status/<int:id>',endpoint = 'Status')
