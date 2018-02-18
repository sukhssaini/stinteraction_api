from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api
import os

app = Flask(__name__)
api = Api(app)

app.config['MONGO_URI'] = "mongodb://rsuser:qwerty741258@ds239648.mlab.com:39648/stinteraction"

mongo = PyMongo(app)

from api.resources.healthcheck import HealthCheck

api.add_resource(HealthCheck, "/check")
