from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class NewsArticle(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80),nullable = False)
    article = db.Column(db.String(700), nullable = False)
    status = db.Column(db.Integer, nullable = False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable = False)

    def __init__(self,article,status):
        self.title = title
        self.article = article
        self.status = status

class Topics(db.Model):
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key = True)
    topicname = db.Column(db.String(50), nullable = False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable = False)

    def __init__(self, topicname):
        self.topicname = topicname

class NewsStatus(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key = True)
    statuscode = db.Column(db.String(10),nullable = False)
    creation_date = db.Column(db.TIMESTAMP, server_default = db.func.current_timestamp(), nullable = False)

    def __init__(self, statuscode):
        self.statuscode = statuscode

class NewsTopic(db.Model):
    __tablename__='newstopic'
    id = db.Column(db.Integer, primary_key = True)
    idNews = db.Column(db.Integer, nullable = False)
    idTopic = db.Column(db.Integer, nullable = False)
    creation_date = db.Column(db.TIMESTAMP, server_default = db.func.current_timestamp(), nullable = False)

    def __init__(self, idNews, idTopic):
        self.idNews = idNews
        self.idTopic = idTopic

class NewsArticleSchema(ma.Schema):
    id = fields.Integer()
    title = fields.String()
    article = fields.String()
    status = fields.Integer()
    creation_date = fields.DateTime()

class TopicsSchema(ma.Schema):
    id = fields.Integer()
    topicname = fields.String()
    creation_date = fields.DateTime()
    
class NewsStatusSchema(ma.Schema):
    id = fields.Integer()
    statuscode = fields.String()
    creation_date = fields.DateTime()

class NewsTopicSchema(ma.Schema):
    id = fields.Integer()
    idNews = fields.Integer()
    idTopic = fields.Integer()
    creation_date = fields.DateTime()

