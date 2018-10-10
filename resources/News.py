from flask_restful import Resource
from flask import request
from Model import db, NewsArticle, NewsArticleSchema

NewsArticle_schemas = NewsArticleSchema(many=True)
NewsArticle_schema = NewsArticleSchema()

class News(Resource):

	# Get All News From News Table
	def get(self):
		news = NewsArticle.query.all()
		newses = NewsArticle_schemas.dump(status).data
		return {'status': 'success', 'data': newses}, 200

	# Post Data To Insert New News
	def post(self):
		json_data = request.get_json(force=True)
		if not json_data:
			return{'message': 'No input data provided'}, 400
		# do validation and deserialize data
		data, errors = NewsArticle_schema.load(json_data)

		if errors:
			return error, 422
		news = NewsArticle.query.filter_by(title=data['title']).first()

		if news:
			return {'message': 'News Already Exists'},400
		news = NewsArticle(title = json_data['title'],article = json_data['article'],status = json_data['status'])
		db.session.add(news)
		db.session.commit()
		result = NewsArticle_schema.dump(news).data
		return {'status': 'success','data':result},201

	# Edit News 
	def put(self):
		json_data = request.get_json(force=True)
		if not json_data:
			return {'message': 'No input data provided'},400
		# Validation and deserialization
		data, errors = NewsArticle_schema.load(json_data)
		if errors:
			return errors, 422

		news = NewsArticle.query.filter_by(id=data['id']).first()

		if not news:
			return {'message': 'News does Not Exists'},400

		news.title = data['title']
		news.article = data['article']
		news.status = data['status']
		db.session.commit()
		result = NewsArticle_schema.dump(news).data	
		return {"status": 'success', 'data': result},204

	# Delete News
	def delete(self):
		json_data = request.get_json(force=True)
		if not json_data:
			return {'message': 'No input data provided'},400
		data, errors = NewsArticle_schema.load(json_data)
		if errors:
			return errors,422
		news = NewsArticle.query.filter_by(id=data['id']).delete()
		if not news:
			return{'message': 'News Already Deleted'},400
		db.session.commit()
		result = NewsArticle_schema.dump(status).data
		return {"status": 'success', "data": result}, 204