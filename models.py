import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:3306/staplerdb'
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)

class Topic(db.Model):
    tid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    desc = db.Column(db.String(120))
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc


class Link(db.Model):
    lid = db.Column(db.Integer, primary_key=True)
    fk_tid = db.Column(db.Integer)
    url = db.Column(db.String(300), unique=True)
    def __init__(self, fk_tid,  url):
        self.fk_tid = fk_tid
        self.url = url


