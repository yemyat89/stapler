from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/staplerdb'
db = SQLAlchemy(app)

class Topic(db.Model):
    tid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    desc = db.Column(db.String(120))
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc


class View(db.Model):
    vid = db.Column(db.Integer, primary_key=True)
    fk_tid = db.Column(db.Integer)
    name = db.Column(db.String(80), unique=True)
    def __init__(self, fk_tid, name):
        self.fk_tid = fk_tid
        self.name = name


class Section(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    fk_vid = db.Column(db.Integer)
    desc = db.Column(db.String(120), unique=True)
    def __init__(self, fk_vid, desc):
        self.fk_vid = fk_vid
        self.desc = desc


class Link(db.Model):
    lid = db.Column(db.Integer, primary_key=True)
    fk_sid = db.Column(db.Integer)
    title = db.Column(db.String(80), unique=True)
    url = db.Column(db.String(300), unique=True)
    def __init__(self, fk_sid, title, url):
        self.fk_sid = fk_sid
        self.title = title
        self.url = url












