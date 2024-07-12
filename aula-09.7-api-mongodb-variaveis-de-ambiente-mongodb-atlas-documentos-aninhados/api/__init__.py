from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config["MONGO_URI"] = f'mongodb+srv://{os.getenv("DB_USER")}:{os.getenv("DB_PASS")}@cluster0.0fbo3m5.mongodb.net/{os.getenv("DB_NAME")}?retryWrites=true&w=majority&appName=Cluster0'

api = Api(app)
mongo = PyMongo(app)
ma = Marshmallow(app)

from .views import games_views