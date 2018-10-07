from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class NewsArticle(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key = True)
    article = db.Column(db.String(700), nullable = False)
    status = db.Column(db.Integer, nullable = False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable = False)

    def __init__(self,article,status):
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

# TODO : Need to Add Schema for validation


# class Comment(db.Model):
#     __tablename__ = 'comments'
#     id = db.Column(db.Integer, primary_key=True)
#     comment = db.Column(db.String(250), nullable=False)
#     creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
#     category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
#     category = db.relationship('Category', backref=db.backref('comments', lazy='dynamic' ))

#     def __init__(self, comment, category_id):
#         self.comment = comment
#         self.category_id = category_id


# class Category(db.Model):
#     __tablename__ = 'categories'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(150), unique=True, nullable=False)

#     def __init__(self, name):
#         self.name = name


# class CategorySchema(ma.Schema):
#     id = fields.Integer()
#     name = fields.String(required=True)


# class CommentSchema(ma.Schema):
#     id = fields.Integer(dump_only=True)
#     category_id = fields.Integer(required=True)
#     comment = fields.String(required=True, validate=validate.Length(1))
#     creation_date = fields.DateTime()