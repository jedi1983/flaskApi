from flask_restful import Resource
from flask import request
from Model import db, NewsArticle, NewsArticleSchema

NewsArticle_schemas = NewsArticleSchema(many=True)
NewsArticle_schema = NewsArticleSchema()

class NewsByStatus(Resource):

	# Get The News By Status ID
	def get(self,id):
		news = NewsArticle.query.filter_by(status=id)
		result = NewsArticle_schemas.dump(news).data
		return {'status': 'success','data':result},200
