from flask_restful import Resource
from app import app, api

class Index(Resource):
    def get(self):
        return {'message': 'Hey there Bob!'}

api.add_resource(Index, '/')
