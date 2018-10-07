from flask_restful import Resource


class News(Resource):
    def get(self):
        return {"message": "Hello, World!"}