from flask_restful import Resource
from sqlalchemy.orm import load_only
from flask import request
from Model import db, NewsArticle, NewsArticleSchema, NewsTopic, NewsTopicSchema

NewsTopic_Schemas = NewsTopicSchema(many=True)
NewsTopic_Schema = NewsTopicSchema()

NewsArticle_Schemas = NewsArticleSchema(many = True)
NewsArticle_Schema = NewsArticleSchema()

class NewsByTopic(Resource):

	def get(self,topic):
		datax = []
		for x in topic:
			if x !=',' and x != '"' :
				datax.append(int(x))

		# Get News ID with Topic Stated
		newsID = NewsTopic.query.filter(NewsTopic.idTopic.in_(datax))
		xData = NewsTopic_Schemas.dump(newsID).data
		del datax [:]
		for x in xData:
			datax.append(x['idNews'])
		Article = NewsArticle.query.filter(NewsArticle.id.in_(datax))
		datas = NewsArticle_Schemas.dump(Article).data
		return {'status': 'success', 'data': datas}, 200

