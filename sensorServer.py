from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

class Driveway(Resource):
	def get(self):
		data = 'Driveway'
		return {'data': data}, 200


api.add_resource(Driveway, '/driveway')

if __name__ == '__main__':
	app.run()
