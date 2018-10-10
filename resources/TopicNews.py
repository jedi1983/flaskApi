from flask_restful import Resource
from flask import request
from Model import db, NewsArticle, NewsArticleSchema
from Model import db, NewsTopic, NewsTopicSchema, NewsTopicAddedSchema

NewsArticle_schemas = NewsArticleSchema(many=True)
NewsArticle_schema = NewsArticleSchema()

NewsTopic_schemas = NewsTopicSchema(many=True)
NewsTopic_schema = NewsTopicSchema()

NewsTopicMany_schemas = NewsTopicAddedSchema()


class TopicNews(Resource):

	# add some new topic to list
	def post(self):
		json_data = request.get_json(force=True)
		if not json_data:
			return{'message': 'No input data provided'}, 400
		# do validation and deserialize data
		data, errors = NewsTopicMany_schemas.load(json_data)

		if errors:
			return error, 422

		newsId = json_data['idNews']
		listOfIdTopic = json_data['idTopic']
		listWillBeAdded = []
		tmp = ''
		for x in listOfIdTopic:
			if x != ',':
				tmp = x
				listWillBeAdded.append(int(x))

		for dataInsert in listWillBeAdded:

			news = NewsTopic(idTopic = dataInsert,idNews = newsId)
			db.session.add(news)
			db.session.commit()
			
		result = NewsTopicMany_schemas.dump(data).data
		return {'status': 'success','data':result},201	
