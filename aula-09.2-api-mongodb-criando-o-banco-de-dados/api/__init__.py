from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb://localhost:27017/apigames'

api = Api(app)
mongo = PyMongo(app)

from .views import games_views