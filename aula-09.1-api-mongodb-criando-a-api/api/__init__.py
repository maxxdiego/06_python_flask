from flask import Flask
from flask_restful import Api

app = Flask(__name__)

api = Api(app)

from .views import games_views