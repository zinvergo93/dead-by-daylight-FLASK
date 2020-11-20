from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmall import Marshmallow
import os


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config("SQLALCHEMY_DATABASE_URI") = "sqlite:///" + os.path.join(
    basedir, "app.sqlite"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma + Marshmallow(app)


class SurvivorPerks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
