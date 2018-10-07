from flask_restful import Resource

class Topic(Resource):
	def get(self):
		return {'message' : 'this is topic'}