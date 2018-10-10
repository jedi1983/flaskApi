from flask_restful import Resource
from flask import request
from Model import db, NewsArticle, NewsArticleSchema
from Model import db, NewsTopic, NewsTopicSchema


class NewsByTopic(Resource):

	# Find News By Category Topic ID and Status
	def post(self,id):
		# Find News By Status ID (draft,release,delete)
		if id == 1:
			pass
		# Find News By Topic Category Id (1,2,3) anything
		elif id == 2:
			pass

