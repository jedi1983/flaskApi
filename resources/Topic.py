from flask import request
from flask_restful import Resource
from Model import db, Topics, TopicsSchema

Topics_schemas = TopicsSchema(many=True)
Topics_schema = TopicsSchema()

class Topic(Resource):
	# Get Data From Status Table
	def get(self):
		topic = Topics.query.all()
		topic = Topics_schemas.dump(topic).data
		return {'status': 'success', 'data': topic}, 200

	# Post Data to Status Table
	def post(self):
		json_data = request.get_json(force=True)
		if not json_data:
			return{'message': 'No input data provided'}, 400
		# do validation and deserialize data
		data, errors = Topics_schema.load(json_data)

		if errors:
			return errors, 422
		topic = Topics.query.filter_by(topicname=data['topicname']).first()

		if topic:
			return {'message': 'Topicname Alread Exists'},400
		topic = Topics(topicname = json_data['topicname'])
		db.session.add(topic)
		db.session.commit()
		result = Topics_schema.dump(topic).data
		return {'status': 'success','data':result},201

	# Edit Status 
	def put(self):
		json_data = request.get_json(force=True)
		if not json_data:
			return {'message': 'No input data provided'},400
		# Validation and deserialization
		data, errors = Topics_schema.load(json_data)
		if errors:
			return errors, 422

		topic = Topics.query.filter_by(id=data['id']).first()

		if not topic:
			return {'message': 'Topicname does Not Exists'},400

		topic.topicname = data['topicname']
		db.session.commit()
		result = Topics_schema.dump(topic).data	
		return {"status": 'success', 'data': result},204

	# Delete Status 
	def delete(self):
		json_data = request.get_json(force=True)
		if not json_data:
			return {'message': 'No input data provided'},400
		data, errors = Topics_schema.load(json_data)
		if errors:
			return errors,422
		topic = Topics.query.filter_by(id=data['id']).delete()
		if not topic:
			return{'message': 'Topicname Already Deleted'},400
		db.session.commit()
		result = Topics_schema.dump(topic).data
		return {"status": 'success', "data": result}, 204
	