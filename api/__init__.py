from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api
import os

app = Flask(__name__)
api = Api(app)

app.config['MONGO_DBNAME'] = os.environ.get("DATABASE_NAME")
app.config['MONGO_URI'] = os.environ.get("MONGO_CONNECTION_URI")

mongo = PyMongo(app)

from api.resources.hello import Hello

api.add_resource(Hello, "/check")
