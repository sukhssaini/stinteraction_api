from flask_restful import Resource
from api.models.error import Error
from flask import jsonify, request

class User(Resource):
    def get(self):
        user_email = request.args.get('user_email')
        if user_email is not None:
            return jsonify({ "name" : "test" })
        else:
            return jsonify(Error(error="user_email cannot be empty or null", status_code=404).serialize())