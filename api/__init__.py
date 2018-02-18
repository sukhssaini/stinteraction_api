from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

app.config['MONGO_DBNAME'] = 'test1'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test1'

mongo = PyMongo(app)

from api.resources.hello import Hello

api.add_resource(Hello, "/check")
