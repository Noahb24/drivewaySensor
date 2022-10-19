from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import database
from datetime import datetime, date

app = Flask(__name__)
api = Api(app)

class Driveway(Resource):
	def get(self):
		sql = """
			SELECT
				id, time, notes
			FROM
				driveway_sensor
		"""
		results = database.fetchAll(sql, {})
		return {'data': results}, 200

	def post(self):
		new = database.fetchOne("""
			INSERT INTO
				driveway_sensor (
					time
				) VALUES (
					'{time}'
				)
			RETURNING id, time, notes;
			""", {'time': datetime.datetime.now()})

		return {'data': {'id': new[0], 'time': new[1], 'notes':new[2]}}, 200

api.add_resource(Driveway, '/driveway')

if __name__ == '__main__':
	app.run()
