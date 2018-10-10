from flask_restful import Resource
from flask import request
from Model import db, NewsArticle, NewsArticleSchema
from Model import db, NewsTopic, NewsTopicSchema

NewsArticle_schemas = NewsArticleSchema(many=True)
NewsArticle_schema = NewsArticleSchema()

NewsTopic_schemas = NewsTopicSchema(many=True)
NewsTopic_schema = NewsTopicSchema()


class TopicNews(Resource):

	# get all topic available
	def get(self):
		news = NewsArticle.query.all()
		newses = NewsArticle_schemas.dump(status).data
		return {'status': 'success', 'data': newses}, 200

	# put some topic tag to news
	def put(self):
		pass

	# add some new topic to list
	def post(self):
		pass

	# delete a topic
	def delete(self):
		pass