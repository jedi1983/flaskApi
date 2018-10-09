from flask import request
from flask_restful import Resource
from Model import db, NewsStatus, NewsStatusSchema

NewsStatus_schemas = NewsStatusSchema(many=True)
NewsStatus_schema = NewsStatusSchema()

class Status(Resource):

	# Get Data From Status Table
	def get(self):
		status = NewsStatus.query.all()
		statuses = NewsStatus_schemas.dump(status).data
		return {'status': 'success', 'data': statuses}, 200

	# Post Data to Status Table
	def post(self):
		json_data = request.get_json(force=True)
		if not json_data:
			return{'message': 'No input data provided'}, 400
		# do validation and deserialize data
		data, errors = NewsStatus_schema.load(json_data)

		if errors:
			return error, 422
		status = NewsStatus.query.filter_by(statuscode=data['statuscode']).first()

		if status:
			return {'message': 'Status Alread Exists'},400
		status = NewsStatus(statuscode = json_data['statuscode'])
		db.session.add(status)
		db.session.commit()
		result = NewsStatus_schema.dump(status).data
		return {'status': 'success','data':result},201

	# Edit Status 
	def put(self):
		json_data = request.get_json(force=True)
		if not json_data:
			return {'message': 'No input data provided'},400
		# Validation and deserialization
		data, errors = NewsStatus_schema.load(json_data)
		if errors:
			return errors, 422

		status = NewsStatus.query.filter_by(id=data['id']).first()

		if not status:
			return {'message': 'StatusCode does Not Exists'},400

		status.statuscode = data['statuscode']
		db.session.commit()
		result = NewsStatus_schema.dump(status).data	
		return {"status": 'success', 'data': result},204

	# Delete Status 
	def delete(self):
		json_data = request.get_json(force=True)
		if not json_data:
			return {'message': 'No input data provided'},400
		data, errors = NewsStatus_schema.load(json_data)
		if errors:
			return errors,422
		status = NewsStatus.query.filter_by(id=data['id']).delete()
		if not status:
			return{'message': 'StatusCode Already Deleted'},400
		db.session.commit()
		result = NewsStatus_schema.dump(status).data
		return {"status": 'success', "data": result}, 204
	

