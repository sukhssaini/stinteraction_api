from flask_restful import Resource
from flask import jsonify


class HealthCheck(Resource):
    def get(self):
        return jsonify({"status": "ok"})
