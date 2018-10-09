from flask_restful import Resource
from flask import request
from Model import db, NewsArticle, NewsArticleSchema


class News(Resource):
    def get(self):
        return {"message": "Hello, World!"}